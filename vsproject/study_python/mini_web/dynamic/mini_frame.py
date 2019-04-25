
def index():
    return "这是主页"

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    file_name = env['PATH_INFO']
    return 'Hello World'

