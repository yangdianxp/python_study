import re

URL_FUNC_DICT = {}

def route(file_name):
    def set_func(func):
        URL_FUNC_DICT[file_name] = func
        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func

@route("/index.py")
def index():
    with open("./mini_web/templates/index.html", encoding='utf-8') as f:
        return f.read()

@route("/center.py")
def center():
    with open("./mini_web/templates/center.html", encoding='utf-8') as f:
        return f.read()

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = env['PATH_INFO']

    if file_name in URL_FUNC_DICT:
        return URL_FUNC_DICT[file_name]()
    else:
        return 'Hello World 我爱你'

