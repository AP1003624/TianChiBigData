# coding=utf8
# Create by 吴俊 on 2016/3/30

# Data Loading
import pandas as pd
from sklearn import preprocessing

id=[]
duration=[]
protocol_type=[]
service=[]
src_bytes=[]
dst_bytes=[]
urgent=[]
count=[]
srv_count=[]
same_srv_rate=[]
dst_host_count=[]
dst_host_srv_count=[]
dst_host_same_srv_rate=[]
dst_host_same_src_port_rate=[]
labeled=[]
attack_types=[]
data = {}
f=file('../testdata.txt','r')
# 跳过标题行
f.readline()
for each in f.readlines():
    items = each.split(',')
    id.append(items[0])
    duration.append(items[1])
    protocol_type.append(items[2])
    service.append(items[3])
    src_bytes.append(items[4])
    dst_bytes.append(items[5])
    urgent.append(items[6])
    count.append(items[7])
    srv_count.append(items[8])
    same_srv_rate.append(items[9])
    dst_host_count.append(items[10])
    dst_host_srv_count.append(items[11])
    dst_host_same_srv_rate.append(items[12])
    dst_host_same_src_port_rate.append(items[13])
    labeled.append(items[14])
    attack_types.append(items[15])

# print id.__len__()
# print duration.__len__()
# print protocol_type.__len__()
# print service.__len__()
# print src_bytes.__len__()
# print dst_bytes.__len__()
# print urgent.__len__()
# print count.__len__()
# print srv_count.__len__()
# print same_srv_rate.__len__()
# print dst_host_count.__len__()
# print dst_host_srv_count.__len__()
# print dst_host_same_srv_rate.__len__()
# print dst_host_same_src_port_rate.__len__()
# print labeled.__len__()
# print attack_types.__len__()

data['id']=pd.Series(id)
data['duration']=pd.Series(duration)
data['protocol_type']=pd.Series(protocol_type)
data['service']=pd.Series(service)
data['src_bytes']=pd.Series(src_bytes)
data['dst_bytes']=pd.Series(dst_bytes)
data['urgent']=pd.Series(urgent)
data['count']=pd.Series(count)
data['srv_count']=pd.Series(srv_count)
data['same_srv_rate']=pd.Series(same_srv_rate)
data['dst_host_count']=pd.Series(dst_host_count)
data['dst_host_srv_count']=pd.Series(dst_host_srv_count)
data['dst_host_same_srv_rate']=pd.Series(dst_host_same_srv_rate)
data['dst_host_same_src_port_rate']=pd.Series(dst_host_same_src_port_rate)
data['labeled']=pd.Series(labeled)
data['attack_types']=pd.Series(attack_types)
# 生成数据框
df = pd.DataFrame(data=data,
                  columns=['id','duration','src_bytes','dst_bytes','urgent','count',\
                           'srv_count','same_srv_rate','dst_host_count','dst_host_srv_count','dst_host_same_srv_rate','dst_host_same_src_port_rate','protocol_type','service','labeled','attack_types']
                  )
# print df.iloc[0:6,0:4]
x = df.iloc[:,1:11]
y = df.iloc[:,0]
# 标准化
scale_x = preprocessing.scale(x)
print(scale_x)
  
