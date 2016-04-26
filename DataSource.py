# coding=UTF-8
# Create by 吴俊 on 2016/3/26

# readline()每次读取一行，当前位置移到下一行；
# readlines()读取整个文件所有行，保存在一个列表(list)变量中，每行作为一个元素；
# read(size)从文件当前位置起读取size个字节（如果文件结束，就读取到文件结束为止），如果size是负值或省略，读取到文件结束为止，返回结果是一个字符串。


# tianchi_fresh_comp_train_item_2w
#  item_id 商品标识
#  item_geohash 商品位置的空间标识，可以为空
#  item_category 商品分类标识

f = open('F:\\TianChiBigData\\new_user\\fresh_comp_offline\\tianchi_fresh_comp_train_item.csv','r')
list=f.readlines()
print(list.__len__())
# for line in list:
#     # strip()类似于java里面的trim()函数
#     # s.strip(rm):去除s开头和结尾处的rm，lstrip(rm)去除开头处,rstrip(rm)去除结尾处的
#     item_id,item_geohash,item_category=line.rstrip('\n').split(',')
#     if(item_id=='item_id' and item_geohash=='item_geohash'and item_category=='item_category'):
#         continue
#     else:
#         print(item_id,item_geohash,item_category)


# tianchi_fresh_comp_train_user_2w
# user_id  用户标识
# item_id  商品标识
# behavior_type  用户对商品的行为类型  包括浏览、收藏、加购物车、购买，对应取值分别是1、2、3、4。
# user_geohash  用户位置的空间标识，可以为空
# item_category 商品分类标识
# time 行为时间
#
# f = open('F:\\TianChiBigData\\new_user\\fresh_comp_offline\\tianchi_fresh_comp_train_user.csv','r')
# list=f.readlines()
# print(list.__sizeof__())
# for line in list:
#     print(line)
#     # 去除结尾处的换行符并进行切割每一列
#     user_id,item_id,behavior_type,user_geohash,item_category,time=line.rstrip('\n').split(',')
#     if(user_id=='user_id' and item_id=='item_id' and behavior_type=='behavior_type' and user_geohash=='user_geohash' and item_category=='item_category' and time=='time'):
#         continue
#     else:
#         print(user_id,item_id,behavior_type,user_geohash,item_category,time)
