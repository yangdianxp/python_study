import re
from pymysql import connect

URL_FUNC_DICT = {}

def route(file_name):
    def set_func(func):
        URL_FUNC_DICT[file_name] = func
        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func

@route(r"/index.html")
def index(ret):
    with open("./mini_web/templates/index.html", encoding='utf-8') as f:
        content = f.read()
    #my_stock_info = "哈哈哈哈 这是你的本月名称......"
    #content = re.sub(r"\{%content%\}", my_stock_info, content)
    conn = connect(host = 'localhost', port = 3306, user = 'root', database = 'stock_db', password = '123456', charset = 'utf8')
    cs = conn.cursor()
    cs.execute("select * from info;")
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()
    tr_template = """<tr>
            <th>{}</th>
            <th>{}</th>
            <th>{}</th>
            <th>{}</th>
            <th>{}</th>
            <th>{}</th>
            <th>{}</th>
            <th>{}</th>
            <td>
                <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="{}">
            </td>
        </tr>"""
    html = ""
    for line_info in stock_infos:
        html += tr_template.format(line_info[0], line_info[1], line_info[2], line_info[3], 
                                   line_info[4], line_info[5], line_info[6], line_info[7], line_info[1])

    content = re.sub(r"\{%content%\}", html, content)
    return content

@route(r"/center.html")
def center(ret):
    with open("./mini_web/templates/center.html", encoding='utf-8') as f:
        content = f.read()
    #my_stock_info = "这里是从mysql查询出来的数据..."
    #content = re.sub(r"\{%content%\}", my_stock_info, content)
    conn = connect(host = 'localhost', port = 3306, user = 'root', database = 'stock_db', password = '123456', charset = 'utf8')
    cs = conn.cursor()
    cs.execute("select i.code, i.short, i.chg, i.turnover, i.price, i.highs, f.note_info from info as i inner join focus as f on i.id = f.info_id;")
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()
    tr_template = """<tr>
	            <th>{}</th>
	            <th>{}</th>
	            <th>{}</th>
	            <th>{}</th>
	            <th>{}</th>
	            <th>{}</th>
	            <th>{}</th>
	            <th>
		            <a type="button" class="btn btn-default btn-xs" href="/update/{}.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
	            </th>
	            <th>
		            <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="{}">
	            </th>
            </tr>
        """
    html = ""
    for line_info in stock_infos:
        html += tr_template.format(line_info[0], line_info[1], line_info[2], line_info[3], 
                                   line_info[4], line_info[5], line_info[6], line_info[0], line_info[0])

    content = re.sub(r"\{%content%\}", html, content)
    return content

@route(r"/add/(\d+)\.html")
def add_focus(ret):
    stock_code = ret.group(1)
    conn = connect(host = 'localhost', port = 3306, user = 'root', database = 'stock_db', password = '123456', charset = 'utf8')
    cs = conn.cursor()
    sql = """select * from info where code = %s"""
    cs.execute(sql, (stock_code, ))
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "没有这支股票，大哥，我们是创业公司，请手下留情..."
    sql = """select * from info as i inner join focus as f on i.id = f.info_id where i.code = %s"""
    cs.execute(sql, (stock_code, ))
    if cs.fetchone():
        cs.close()
        conn.close()
        return "已经关注过了，请勿重复关注"
    sql = """insert into focus (info_id) select id from info where code = %s"""
    cs.execute(sql, (stock_code, ))
    conn.commit()
    cs.close()
    conn.close()
    return "关注成功..."

@route(r"/del/(\d+)\.html")
def del_focus(ret):
    stock_code = ret.group(1)
    conn = connect(host = 'localhost', port = 3306, user = 'root', database = 'stock_db', password = '123456', charset = 'utf8')
    cs = conn.cursor()
    sql = """select * from info where code = %s"""
    cs.execute(sql, (stock_code, ))
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "没有这支股票，大哥，我们是创业公司，请手下留情..."
    sql = """select * from info as i inner join focus as f on i.id = f.info_id where i.code = %s"""
    cs.execute(sql, (stock_code, ))
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "{} 之前未关注，请勿取消关注...".format(stock_code)
    sql = """delete from focus where info_id = (select id from info where code = %s)"""
    cs.execute(sql, (stock_code, ))
    conn.commit()
    cs.close()
    conn.close()
    return "取消关注成功..."

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = env['PATH_INFO']

    try: 
        #func = URL_FUNC_DICT[file_name]
        #return func()
        for url, func in URL_FUNC_DICT.items():
            ret = re.match(url, file_name)
            if ret:
                return func(ret)
        else:
            return "请求的url({})没有对应的函数。。。".format(file_name)
    except Exception as ret:
        return "产生了异常: {}".format(ret)


