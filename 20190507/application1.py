'''此文件实现的是应用程序框架'''

import time


def handlertime():
    '''这个函数用来处理时间的获取'''
    time_data = time.ctime()
    return time_data


def score():
    count = 66
    '''这个函数用来返回学生的考试成绩'''
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    <h1>your score:%s</h1>
    
    </body>
    </html>
    
    ''' % count
    return html


urllist = [
    ('/time.py', handlertime),
    ('/score.py', score)
]


# WSGI接口
# def app(environ,start_response):
#     print('environ:',environ)
#     request_path = environ['path']
#     print(request_path)
#     for path,ff in urllist:
#         if path == request_path:
#             start_response('200 ok', [('server', 'wsgisever'), ('name', 'guazi'), ('request_path', request_path)])
#             return ff
#     else:
#         start_response('200 ok', [('server', 'wsgisever'), ('name', 'guazi'), ('request_path', request_path)])
#         return '资源不存在'


class AppClass():
    def __init__(self):
        pass

    def __call__(self, environ, start_response):
        print('environ:', environ)
        request_path = environ['path']
        print(request_path)
        for path, ff in urllist:
            if path == request_path:
                data = ff()
                start_response('200 ok', [('server', 'wsgisever'), ('name', 'guazi'), ('request_path', request_path)])
                return data
        else:
            start_response('200 ok', [('server', 'wsgisever'), ('name', 'guazi'), ('request_path', request_path)])
            return '资源不存在'


app = AppClass()
