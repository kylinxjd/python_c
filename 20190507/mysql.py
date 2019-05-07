import pymysql

connect_obj = pymysql.connect(host='localhost',
                              port=3306,
                              database='python',
                              user='root',
                              password='123456')
print(connect_obj)
# 获取可操作对象pymysql.cursors.DictCursor
cur = connect_obj.cursor()

sql = 'select * from student'

# 返回记录条数
count = cur.execute(sql)
# print(count)
# data = cur.fetchall()
data1 = cur.fetchone()
data2 = cur.fetchone()
data = cur.fetchall()
print(data1)
print(data2)
print(data)
print(type(data))
print(type(str(data)))

with open('index.html') as f:
    responsebody = f.read()
print(type(responsebody))
