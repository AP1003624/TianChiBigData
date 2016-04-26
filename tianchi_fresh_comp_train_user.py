# coding=utf8
# Create by 吴俊 on 2016/3/27

import MySQLdb
import time

conn = MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '123456',
    db = 'tianchi_fresh_comp',
    charset = 'utf8'
)

cur = conn.cursor()
try:
    # cur.execute('drop table if is exists tianchi_fresh_comp_train_user')
    cur.execute('CREATE TABLE tianchi_fresh_comp_train_user(id int not null PRIMARY key AUTO_INCREMENT,\
                user_id INT not NULL,\
                item_id int not NULL,\
                behavior_type int not NULL,\
                user_geohash int NULL,\
                item_category int not NULL,\
                time VARCHAR(25) not NULL) ')
except:
    print('建表失败！')
    conn.rollback()
conn.commit()
print('建表成功！')


f = open('F:\\TianChiBigData\\new_user\\fresh_comp_offline\\tianchi_fresh_comp_train_user.csv','r')
list=f.readlines()
print(list.__le__())
for line in list:
    # 去除结尾处的换行符并进行切割每一列
    user_id,item_id,behavior_type,user_geohash,item_category,time=line.rstrip('\n').split(',')
    value = []
    if(user_id=='user_id' and item_id=='item_id' and behavior_type=='behavior_type' and user_geohash=='user_geohash' and item_category=='item_category' and time=='time'):
        continue
    else:
        try:
            if(user_geohash == ' '):
                value.append(user_id)
                value.append(item_id)
                value.append(behavior_type)
                value.append(user_geohash)
                value.append(item_category)
                value.append(time)
                cur.execute('insert into tianchi_fresh_comp_train_user(user_id,item_id,behavior_type,user_geohash,item_category,time) value(%d,%d,%d,%d,%d,%s)',value)
            else:
                value.append(user_id)
                value.append(item_id)
                value.append(behavior_type)
                value.append(item_category)
                value.append(time)
                cur.execute('insert into tianchi_fresh_comp_train_user(user_id,item_id,behavior_type,item_category,time) value(%d,%d,%d,%d,%s)',value)
        except:
            print('插入数据出现问题！')
            conn.rollback()
            break;
        conn.commit()
try:
    result = cur.execute('select count(*) from tianchi_fresh_comp_train_user')
    print('总共插入 '+str(result)+' 条数据！')
except:
    print('查询数据表总数据失败！')
cur.close()
conn.commit()
conn.close()



