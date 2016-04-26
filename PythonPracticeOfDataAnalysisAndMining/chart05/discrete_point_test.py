# coding=utf8
# Create by 吴俊 on 2016/4/25

# 代码清单5-8 离群点检测
# 使用K_means算法聚类消费行为特征数据
import numpy as np
import pandas as pd

# 参数初始化
# 销售及其他属性数据
inputFile = u'data/consumption_data.xls'
# 聚类的类别
K = 3
# 离散点阈值
threshold = 2
# 聚类最大循环次数
iteration = 500
# 读取数据
data = pd.read_excel(inputFile,index_col='Id')
# 数据标准化
data_zs = 1.0*(data-data.mean())/data.std()

# 开始聚类
from sklearn.cluster import KMeans
model = KMeans(n_clusters=K,max_iter=iteration)
model.fit(data_zs)

# 标准化数据及其类别
r = pd.concat([data_zs,pd.Series(model.labels_,index=data_zs.index)],axis=1)
r.columns = list(data.columns)+[u'聚类类别']
norm = []
# 逐一处理
for i in range(K):
    norm_temp = r[['R','F','M']][r[u'聚类类别']==i]-model.cluster_centers_[i]
    # 求出绝对距离
    norm_temp = norm_temp.apply(np.linalg.norm,axis=1)
    # 求相对距离并添加
    norm.append(norm_temp/norm_temp.median())

# 合并
norm = pd.concat(norm)

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

# 正常点
norm[norm<=threshold].plot(style='go')
# 离散点
discrete_points = norm[norm>threshold]
discrete_points.plot(style='ro')

# 离群点做标记
for i in range(len(discrete_points)):
    id = discrete_points.index[i]
    n = discrete_points.iloc[i]
    plt.annotate('(%s,%0.2f)' %(id,n),xy=(id,n),xytext=(id,n))
plt.xlabel(u'编号')
plt.ylabel(u'相对距离')
plt.show()
