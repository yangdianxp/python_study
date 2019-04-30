import re

URL_FUNC_DICT = {}

def route(file_name):
    def set_func(func):
        URL_FUNC_DICT[file_name] = func
        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func

@route("/index.html")
def index():
    with open("./mini_web/templates/index.html", encoding='utf-8') as f:
        content = f.read()
    #my_stock_info = "哈哈哈哈 这是你的本月名称......"
    #content = re.sub(r"\{%content%\}", my_stock_info, content)
    conn = connect(host = 'localhost', port = 3306, user = 'root', database = 'stock_db', charset = 'utf8')
    cs = conn.cursor()
    cs.execute("select * from info;")
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()
    content = re.sub(r"\{%content%\}", str(stock_infos), content)
    return content

@route("/center.html")
def center():
    with open("./mini_web/templates/center.html", encoding='utf-8') as f:
        content = f.read()
    my_stock_info = "这里是从mysql查询出来的数据..."
    content = re.sub(r"\{%content%\}", my_stock_info, content)
    return content

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = env['PATH_INFO']

    try: 
        func = URL_FUNC_DICT[file_name]
        return func()
    except Exception as ret:
        return "产生了异常: {}".format(ret)


