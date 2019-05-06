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

    def change_password(self):
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
        sql = 'select goods.id, goods.name, goods.price, cate.name, brande.name from (goods INNER JOIN cate ON goods.cate_id=cate.id INNER JOIN brande ON goods.brande_id=brande.id)'
        self.cur.execute(sql)
        goods = self.cur.fetchall()
        print('所有商品展示：')
        for g in goods:
            print(g)

    def order(self):
        if self.islogin:
            inID = input('请输入您要购买的产品的ID：')
            sql1 = 'select * from goods WHERE is_selt=0 AND id=%s'
            count = self.cur.execute(sql1, [inID])
            if count==0:
                print("该商品已经卖出")
                return
            else:
                sql2 = 'insert into order_m VALUES (0,%s,%s,%s,%s)'
                self.cur.execute('select price from goods WHERE id=%s', [inID])
                cost = self.cur.fetchall()
                # print(cost)
                # print(type(cost))
                # print(type(cost[0]))
                # print(type(cost[0][0]))
                cou = self.cur.execute('select serial_number from order_m ORDER BY id DESC limit 1')
                if cou == 0:
                    self.cur.execute(sql2,[self.name, inID, cost[0][0], 10010])
                else:
                    serial_num = self.cur.fetchall()
                    # print(serial_num)
                    # print(type(serial_num))
                    # print(type(serial_num[0]))
                    # print(type(serial_num[0][0]))
                    self.cur.execute(sql2, [self.name, inID, cost[0][0], int(serial_num[0][0])+1])
                self.cur.execute('select name from goods WHERE id=%s', [inID])
                good_name = self.cur.fetchall()
                self.cur.execute('update goods set is_selt=1 WHERE id=%s',[inID])
                self.connect.commit()
                print("下单成功，购买"+good_name[0][0]+"花费", cost[0][0], "元")
            return
        else:
            print("您还没有登录")
            return

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
                self.change_password()

            elif choose == '6':
                break

            else:
                print('输入错误')


if __name__ == '__main__':
    shanghui = ShangHui()
    shanghui.printinfo()
