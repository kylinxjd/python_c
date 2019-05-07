import socket
import sys
import pymysql
import re
import chardet


class Socket():
    def __init__(self, port, app):
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(("", self.port))
        self.server_socket.listen(5)
        self.reponse_data = None
        self.app = app
        # 连接数据库
        self.connect = pymysql.connect(host='localhost', port=3306,
                                       database='python', user='root', password='123456', charset='utf8')
        self.cur = self.connect.cursor()
        self.islogin = False   # 判断登录状态
        self.name = None       # 用户名
        self.password = None   # 密码
        self.buyid = None      # 购买商品的ID
        self.rname = None      # 注册名称
        self.psd = None        # 注册密码

    def creat(self, c_s_socket):
        while True:
            # 2.在三次握手完成后，为客户端套接字创建客服
            c_s_socket, addressinfo = self.server_socket.accept()
            # self.handler(c_s_socket)
            # 3.浏览器向服务器发送请求报文,服务器接收报文
            data = c_s_socket.recv(1024).decode()
            # print(data)
            # data是接收到的浏览器请求报文,并且是二进制文件
            ret = data.split("\r\n")
            # j=0
            # print("##########################@")
            # for i in ret:
            #     print(j)
            #     j+=1
            #     print(i)
            # print("#############################")

            # 判断登录  15会抛出out of range，get请求没有15行
            if ret[0] == 'POST /index HTTP/1.1':
                userpass = ret[15]
                print("----------------------------")
                print(userpass)
                print("----------------------------")
                # username=sssss&password=sss
                userlist = userpass.split('&')
                self.name = userlist[0].split('=')[1]
                self.password = userlist[1].split('=')[1]
                # 判断登录
                sqlm = 'select * from user where name=%s and password=%s'
                retm = self.cur.execute(sqlm, [self.name, self.password])
                if retm == 0:
                    self.islogin = False
                else:
                    self.islogin = True
                    # print(self.name)
                    # print(self.password)
            elif ret[0] == 'POST /buy.py HTTP/1.1':
                buy = ret[15]
                buyId = buy.split('=')[1]
                print(buyId)
                self.buyid = int(buyId)
            elif ret[0] == 'POST /rsubmit HTTP/1.1':
                reg = str(ret[15]).strip()
                #     username=admin&password=zxcv
                print(reg)
                userpass = re.match('username=(.*?)&password=(.*)', reg)
                self.rname = userpass.group(1)
                self.psd = userpass.group(2)

            # 4.服务器根据浏览器发送的报文返回具体响应
            # todo:开始拼接响应报文
            # todo:截取请求的路径，获取请求的具体内容，根据路径不同，返回不同数据
            # 4.0获取请求报文第一行
            request_first_line = ret[0]
            ret2 = request_first_line.split(' ')
            print(ret2)
            try:
                request_path = ret2[1]
            except:
                request_path = '/index'

            environ = {'path': request_path}
            if request_path.endswith('.py'):
                if request_path == '/buy.py':
                    environ['buyid'] = self.buyid
                    environ['is_login'] = self.islogin
                    environ['cur'] = self.cur
                    environ['connect'] = self.connect
                    environ['name'] = self.name
                # 第一步调用框架的接口
                responsebody = self.app(environ, self.start_response)
                rdata = self.reponse_data + responsebody
                # data = self.reponse_data + "as"
                c_s_socket.send(rdata.encode('GBK'))
                c_s_socket.close()
            # elif request_path == '/gett':

            else:
                # 根据路径，获得对应数据
                # 首页展示商品
                if request_path == '/index':
                    # formData = request.form
                    # print(formData)
                    status = '200 ok'
                    with open('index.html', 'rb') as f:
                        # responsebody = f.read()
                        responsebody = f.read()
                    ht = responsebody.decode()
                    slist = ht.split('<hr>')
                    sql = 'select goods.id, goods.name, goods.price, cate.name, brande.name from (goods INNER JOIN cate ON goods.cate_id=cate.id INNER JOIN brande ON goods.brande_id=brande.id) WHERE is_selt=0'
                    self.cur.execute(sql)
                    goods = self.cur.fetchall()
                    #     \r\n
                    for g in goods:
                        slist[1] += str(g) + '<br>'
                    # print(slist)
                    # print("--------------------------")
                    # print(len(slist))
                    # print("--------------------------")
                    # print(type(slist[0]+slist[1]+slist[2]))
                    # print("--------------------------")
                    formBuy = """
                    <form action="/buy.py" method="post">
                        <label for="buy">请输入商品ID</label>
                        <input type="text" id="buy" name="buy" placeholder="商品ID">
                        <br><br>
                        <input style="width: 100px; height: 30px" type="submit" id="buy" value="购买">
                    </form>
                    """
                    slist[1] = slist[1] + '<br>' + '<br>' + formBuy + '<br>'
                    res = slist[0] + '<hr>' + slist[1] + '<hr>' + slist[2]
                    print(res)
                    responsebody = res.encode('utf8')
                #     登录页面
                elif request_path == '/login':
                    status = '200 ok'
                    with open('login.html', 'rb') as f:
                        responsebody = f.read()
                #         注册页面
                elif request_path == '/register':
                    status = '200 ok'
                    with open('register.html', 'rb') as f:
                        responsebody = f.read()
                #         注册提交
                elif request_path == '/rsubmit':
                    sql = 'select * from user where name=%s'
                    ret = self.cur.execute(sql, [self.rname])
                    if ret:
                        print('用户名已经存在')
                        req = '用户名已经存在'
                        responsebody = req.encode('utf8')
                    else:
                        # 如果没有则插入数据库
                        sql_insert = 'insert into user VALUES(0,%s,%s)'
                        self.cur.execute(sql_insert, [self.rname, self.psd])
                        # 修改数据库的数据需要提交
                        self.connect.commit()
                        status = '200 ok'
                        with open('rsuccess.html', 'rb') as f:
                            responsebody = f.read()
                elif request_path == '/buy':
                    # self.cur.execute('update goods set is_selt=1 WHERE id=%s', [ID])
                    # self.connect.commit()
                    # 静态购买
                    if self.islogin:
                        sql1 = 'select * from goods WHERE is_selt=0 AND id=%s'
                        count = self.cur.execute(sql1, [self.buyid])
                        if count == 0:
                            print("该商品已经卖出")
                            return
                        else:
                            sql2 = 'insert into order_m VALUES (0,%s,%s,%s,%s)'
                            self.cur.execute('select price from goods WHERE id=%s', [self.buyid])
                            cost = self.cur.fetchall()
                            cou = self.cur.execute('select serial_number from order_m ORDER BY id DESC limit 1')
                            if cou == 0:
                                self.cur.execute(sql2, [self.name, int(self.buyid), cost[0][0], 10010])
                            else:
                                serial_num = self.cur.fetchall()
                                self.cur.execute(sql2, [self.name, self.buyid, cost[0][0], int(serial_num[0][0]) + 1])
                            self.cur.execute('select name from goods WHERE id=%s', [self.buyid])
                            good_name = self.cur.fetchall()
                            self.cur.execute('update goods set is_selt=1 WHERE id=%s', [self.buyid])
                            self.connect.commit()
                            print("下单成功，购买" + good_name[0][0] + "花费", cost[0][0], "元")
                        # self.cur.execute('update goods set is_selt=1 WHERE id=%s', [self.buyid])
                        # self.connect.commit()
                        status = '200 ok'
                        with open('buy.html', 'rb')as f:
                            responsebody = f.read()
                    else:
                        status = '200 ok'
                        with open('err.html', 'rb')as f:
                            responsebody = f.read()
                else:
                    status = '404 not found'
                    with open('err.html', 'rb')as f:
                        responsebody = f.read()

                # 4.1拼接第一行的数据HTTP/1.1 状态码 说明\r\n
                first_line = 'HTTP/1.1' + status + '\r\n'
                first_line += 'name:server\r\n'
                first_line += '\r\n'
                # responsebody='hello world!'
                response = first_line.encode('utf8') + responsebody
                c_s_socket.send(response)
                # 5.人工客服完成任务之后被销毁
                c_s_socket.close()
                # 6.服务器套接字一把那不会关闭

    def start_response(self, status, header_list):
        '''
        这个函数实现的是拼接响应报文，遵循的还是响应报文的格式，请求动态资源的时候调用
        :param status: 状态码。例如：‘200 ok’
        :param header_list: 列表，例如：[(server,wsgiserver)，(name,guazi)]
        :return:
        '''
        response_header_fl = ' HTTP/1.1 %s \r\n' % status
        response_header = ''
        for header_key, header_value in header_list:
            response_header += ('%s:%s\r\n' % (header_key, header_value))
        self.reponse_data = response_header_fl + response_header + '\r\n'


if __name__ == '__main__':
    print('此时获取的参数列表', sys.argv)
    try:
        port = int(sys.argv[1])
        kj_name = sys.argv[2]
        print(kj_name)
    except:
        port = 8080
        kj_name = 'myapp:app'
    finally:
        jiekou_list = kj_name.split(':')
        model_name = jiekou_list[0]
        app_name = jiekou_list[1]
        # __import__的参数是一个字符串形式
        kj_obj = __import__(model_name)
        # getattr()方法：getattr(x, 'y') = x.y
        app = getattr(kj_obj, app_name)
        socket_obj = Socket(port, app)
        socket_obj.creat(socket_obj)
