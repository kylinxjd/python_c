# _*_ coding: utf-8 _*_
"""这个程序执行的模拟商城购物情况"""
import pymysql


class ShangHui(object):
    def __init__(self):
        # 只需要连接一次
        self.connect = pymysql.connect(host='localhost', port=3306,
                                       database='python', user='root', password='123456', charset='utf8')
        self.cur = self.connect.cursor()
        self.islogin = False
        self.name = None
        self.password = None

    def login(self):
        inname = input('请输入用户名')
        inpassword = input('请输入密码')
        # 拼接sql字符串
        sqlm = 'select * from user where name=%s'
        retm = self.cur.execute(sqlm, [inname])
        if retm == 0:
            print('用户名不存在')
            return
        sql = 'select * from user where name=%s and password=%s'
        # sql = 'select * from user where name=inname and password=inpassword'
        # print(sql)
        ret = self.cur.execute(sql, [inname, inpassword])
        # print(ret)
        if ret == 0:
            print('用户名或者密码错误')
            return
        self.islogin = True
        self.name = inname
        self.password = inpassword
        print('########登录成功#############')

    def register(self):
        # 1、判断用户是否在当前的用户表里(保证用户名的唯一性)
        inname = input('请输入用户名')
        inpassword = input('请输入密码')
        sql = 'select * from user where name=%s'
        ret = self.cur.execute(sql, [inname])
        if ret:
            print('用户名已经存在')
            return

        # 2、如果没有则插入数据库
        sql_insert = 'insert into user VALUES(0,%s,%s)'
        self.cur.execute(sql_insert, [inname, inpassword])
        # 3 注意修改数据库的数据需要提交
        self.connect.commit()
        print('注册成功')

    def xiugaimima(self):
        if self.islogin:
            inname = input('请输入用户名')
            inpassword = input('请输入新密码:')
            if self.name != inname:
                print("用户名不匹配!")
            else:
                sql = 'update user set password=%s where name=%s'
                self.cur.execute(sql, [inpassword, self.name])
                self.connect.commit()
                print('######密码修改成功#######')
            return
        else:
            print("您还没有登录")
            return

    def showgood(self):
        print('商品展示')

    def order(self):
        print('下单')

    def printinfo(self):
        print('欢迎来到尚惠有品商城')
        print('1-登录')
        print('2-注册')
        print('3-商品展示')
        print('4-下单')
        print('5-修改密码')
        print('6-退出')

        while True:
            choose = input('请输入需要执行的操作:')
            if choose == '1':
                self.login()

            elif choose == '2':
                self.register()

            elif choose == '3':
                self.showgood()

            elif choose == '4':
                self.order()

            elif choose == '5':
                self.xiugaimima()

            elif choose == '6':
                break

            else:
                print('输入错误')


if __name__ == '__main__':
    shanghui = ShangHui()
    shanghui.printinfo()
