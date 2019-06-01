from flask import Flask, current_app, redirect, url_for, request
from werkzeug.routing import BaseConverter

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
    print(current_app.config.get("ITCAST"))
    name = request.form.get("name")
    age = request.form.get("age")
    print(request.data)
    print(request.args)
    #name = request.data.get("name")
    #age = request.data.get("age")
    return "hello name = {}, age = {}".format(name, age)

@app.route("/post_only", methods=["GET", "POST"])
def post_only():
    return "post only page"

@app.route("/login")
def login():
    #url = "/"
    url = url_for("index")

    return redirect(url)

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
def send_msm(mobile):
    return "send sms to {}".format(mobile) 


if __name__ == '__main__':
    print(app.url_map)
    app.run(host="0.0.0.0", port=5000)
