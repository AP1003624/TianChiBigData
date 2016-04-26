# coding=utf8
# Create by 吴俊 on 2016/3/26

import MySQLdb
# 用于创建数据库的连接，里面可以指定参数：用户名，密码，主机等信息。
conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='kdd_cup99',
    charset='utf8'
)
# 使用cursor()方法获取操作游标
cur = conn.cursor()
# 执行SQL语句
try:
    # 建表
    cur.execute('drop table if EXISTS students')
    cur.execute('create table students(id int not null PRIMARY KEY auto_increment ,name VARCHAR (10),hometown VARCHAR (10))')

    # 插入数据
    list = []
    for i in range(5):
        data = ('吴俊'+str(i),'吴俊'+str(i))
        list.append(data)
    # 批量插入
    result = cur.executemany("insert into students(name,hometown) VALUE(%s,%s)",list)
    if(result == list.__len__()):
        print('批量插入数据成功！')
    else:
        print('批量插入数据失败！')
    # 插入单条数据
    result = cur.execute("insert into students(name,hometown) VALUE(%s,%s)",list.pop(i))

    # 查询所有数据
    cur.execute('select * from  students')
    result = cur.fetchall();
    for each in result:
        print each[0],each[1],each[2]

    # 查询单条数据
    cur.execute('select * from  students')
    result = cur.fetchone();
    print result[0], result[1], result[2]

    # 修改数据
    result = cur.execute("update students set name='吴俊',hometown='吴俊' where id=1")
    if(result == 1):
        print('修改成功！')
    else:
        print('修改失败！')
except:
     print(u"查询出现异常")
print('操作成功！')
# 关闭游标
cur.close()
# 提交事务
conn.commit()
# 关闭数据库连接
conn.close()


