import pymysql

urlfuncdict = {}
connect_obj = pymysql.connect(host='localhost',
                              port=3306,
                              database='python',
                              user='root',
                              password='123456',
                              charset='utf8')


def route(url):
    print(url)

    def wapper(func):
        # 添加键值对
        urlfuncdict[url] = func

        def inner():
            response_body = func()
            return response_body

        return inner

    return wapper


@route("/login.py")
def login():
    with open('index.html') as f:
        responsebody = f.read()
    return responsebody


@route("/mysql.py")
def mysql():
    return "as"


@route("/buy.py")
def buy(islogin, buyid, cur, connect, name):
    if islogin:
        # 检查商品是否有库存
        sql1 = 'select * from goods WHERE is_selt=0 AND id=%s'
        count = cur.execute(sql1, [int(buyid)])
        if count == 0:
            print("该商品已经卖出")
            dat = "该商品已经卖出"
        else:
            sql2 = 'insert into order_m VALUES (0,%s,%s,%s,%s)'
            cur.execute('select price from goods WHERE id=%s', [int(buyid)])
            # 获取商品价格
            cost = cur.fetchall()
            # 获取上一条订单的订单号
            cou = cur.execute('select serial_number from order_m ORDER BY id DESC limit 1')
            if cou == 0:
                # 第一条订单
                cur.execute(sql2, [name, int(buyid), cost[0][0], 10010])
            else:
                serial_num = cur.fetchall()
                # 添加订单
                cur.execute(sql2, [name, buyid, cost[0][0], int(serial_num[0][0]) + 1])
            #     获取商品名称
            cur.execute('select name from goods WHERE id=%s', [buyid])
            good_name = cur.fetchall()
            # 更新商品库存
            cur.execute('update goods set is_selt=1 WHERE id=%s', [buyid])
            connect.commit()
            dat = "下单成功，购买" + good_name[0][0] + "花费" + str(cost[0][0]) + "元"

    else:
        # with open('relogin.html', encoding='utf8')as f:
        #     dat = f.read()
        # print(dat)
        # print(type(dat))
        # dat = '''<!DOCTYPE html>
        # <html lang="en">
        # <head>
        #     <meta charset="UTF-8">
        #     <title>Title</title>
        # </head>
        # <body>
        #     <h1>还没有登录</h1>
        #     <a href="/login">返回登录</a>
        # </body>
        # </html>'''
        dat = "购买失败"
    # data = "购买失败", encoding='utf8'
    return dat


def app(environ, start_response):
    print('environ:', environ)
    request_path = environ['path']
    # print(request_path)
    try:
        start_response('200 ok', [('server', 'wsgisever'), ('name', 'guazi'), ('request_path', request_path)])
        if request_path == '/buy.py':
            # islogin, buyid, cur, connect, name
            response_body = urlfuncdict[request_path](environ['is_login'], environ['buyid'],
                                                      environ['cur'], environ['connect'], environ['name'])
        else:
            response_body = urlfuncdict[request_path]()
        return response_body
    except:
        start_response('404 not', [('server', 'wsgisever'), ('name', 'guazi'), ('request_path', request_path)])
        return '404'
