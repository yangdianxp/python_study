from flask import Flask, current_app, redirect, url_for, request, abort, Response
from flask import make_response
from flask import jsonify
from werkzeug.routing import BaseConverter
import json

# 创建flask的应用对象
# __name__表示当前的模块名字
app = Flask(__name__,
            static_url_path="/python",
            static_folder="static",
            template_folder="templates")

# app.config.from_pyfile("config.cfg")
class Config():
    DEBUG = True
    ITCAST = "python"

app.config.from_object(Config)

# app.config["DEBUG"] = True

# ?后的是查询字符串 QueryString
@app.route("/index", methods=["GET", "POST"])
def index():
    #print(current_app.config.get("ITCAST"))
    #name = request.form.get("name")
    #age = request.form.get("age")
    #print(request.data)
    #print(request.args)
    ##name = request.data.get("name")
    ##age = request.data.get("age")
    #if request.method == 'GET':
    #    pass
    #elif request.method == 'POST':
    #    pass
    ##return "hello name = {}, age = {}".format(name, age), 400, [("Itcast", "python"), ("City", "shenzhen")]
    #resp = make_response('index page 2')
    #resp.status = "999 itcast"
    #resp.headers["city"] = "sz"
    #return resp

    data = {
        "name": "python",
        "age": 18
    }
    #json_str = json.dumps(data)
    #print(json_str)

    #a = """{"city": "sz", "country":"china"}"""
    #d = json.loads(a)
    #print(type(d))
    #print(d)

    #return json_str, 200, {"Content-Type": "application/json"}

    return jsonify(data)


@app.route("/post_only", methods=["GET", "POST"])
def post_only():
    return "post only page"

@app.route("/login")
def login():
    ##url = "/"
    #url = url_for("index")

    #return redirect(url)
    name = request.form.get("name")
    pwd = request.form.get("pwd")
    if name == "zhangsan" and pwd == "admin":
        return "login success"
    else:
        abort(404)
        #resp = Response("login failed")
        #abort(resp)

# 转换器
@app.route("/goods/<int:goods_id>")
def goods_detail(goods_id):
    return "goods detail page {}".format(goods_id)

# 定义自己的转换器
class RegexConverter(BaseConverter):
    def __init__(self, url_map, regex):
        super().__init__(url_map)
        self.regex = regex

    def to_python(self, value):
        pass

    def to_url(self, value):
        pass

# 将自定义的转换器添加到flask的应用中
app.url_map.converters["re"] = RegexConverter

@app.route("/send/<re(r'1[34578]\d{9}'):mobile>")
def send_sms(mobile):
    return "send sms to {}".format(mobile) 

@app.route("/upload", methods=["POST"])
def upload():
    file_obj = request.files.get("pic")
    if file_obj is None:
        return "未上传文件"
    #with open("./demo.jpg", 'wb') as f:
    #    data = file_obj.read() 
    #    f.write(data)
    file_obj.save("demo1.png")
    return "上传成功"

@app.errorhandler(404)
def handle_404_error(err):
    return "handle_404_error"

@app.route("/set_cookie")
def set_cookie():
    resp = make_response("success")
    resp.set_cookie("Itcast", "Python")
    resp.set_cookie("Itcast1", "Python1")
    return resp

if __name__ == '__main__':
    print(app.url_map)
    app.run(host="0.0.0.0", port=5000)
