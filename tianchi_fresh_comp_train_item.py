# coding=utf8
# Create by 吴俊 on 2016/3/26

import MySQLdb

db = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='tianchi_fresh_comp',
    charset='utf8'
)
cur = db.cursor()

try:
    # 建表
    cur.execute('DROP TABLE IF EXISTS tianchi_fresh_comp_train_item')
        # cur.execute('create table tianchi_fresh_comp_train_item(id int not null primary key auto_increment,item_id int not null,item_geohash int NULL,item_category int not null)')
    cur.execute('CREATE TABLE tianchi_fresh_comp_train_item(id int NOT NULL PRIMARY KEY AUTO_INCREMENT,item_id int NOT NULL,item_geohash int NULL ,item_category int NOT NULL)')
    f = open('F:\\TianChiBigData\\new_user\\fresh_comp_offline\\tianchi_fresh_comp_train_item.csv','r')
    list=f.readlines()
    for line in list:
        # strip()类似于java里面的trim()函数
        # s.strip(rm):去除s开头和结尾处的rm，lstrip(rm)去除开头处,rstrip(rm)去除结尾处的
        item_id,item_geohash,item_category=line.rstrip('\n').split(',')
        value = []
        if(item_id=='item_id' and item_geohash=='item_geohash'and item_category=='item_category'):
            continue
        else:
            if(item_geohash ==' '):
                value.append(item_id)
                value.append(item_geohash)
                value.append(item_category)
                cur.execute("insert into tianchi_fresh_comp_train_item(item_id,item_geohash,item_category) value (%s,%s,%s)",value)
                # print(item_id,item_geohash,item_category)
            else:
                value.append(item_id)
                value.append(item_category)
                cur.execute("insert into tianchi_fresh_comp_train_item(item_id,item_category) value (%s,%s)",value)
            db.commit()
except:
    print('操作失败！')
cur.close()
db.commit()
db.close()

