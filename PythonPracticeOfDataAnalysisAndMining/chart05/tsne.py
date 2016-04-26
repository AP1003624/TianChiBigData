# coding=utf8
# Create by 吴俊 on 2016/4/25

# 代码清单5-5 用TSNE进行数据降维并展示聚类结果


# 接 k_means.py

import pandas as pd

# 数据初始化
# 销售及其他属性数据
inputFile = u'data/consumption_data.xls'
# 保存结果的文件名
outFile = 'data/k_means_consumption_data.xls'
import os
# 如果文件存在，则删除
if os.path.exists(outFile):
    os.remove(outFile)
# 聚类的类别
K = 3
# 聚类最大循环次数
iteration = 500
# 读取数据
data = pd.read_excel(inputFile, index_col=u'Id')
# 数据标准化
data_zs = (data - data.mean())/data.std()

from sklearn.cluster import KMeans
# 分为K类，并发数为4，最大迭代计算次数为iteration
model = KMeans(n_clusters = K, max_iter = iteration)
# 开始聚类
model.fit(data_zs)

# 打印结果
# 统计各个类别的数目
r1 = pd.Series(model.labels_).value_counts()
# 找到聚类中心
r2 = pd.DataFrame(model.cluster_centers_)
# 横向连接（0是纵向），得到聚类中心对应的类别下的数目
r = pd.concat([r1,r2],axis=1)
# 重命名表头
r.columns = list(data.columns)+[u'类别数目']

# 详细输出原始数据及其类别
# 输出每个样本对应的类别
r = pd.concat([data,pd.Series(model.labels_,index=data.index)],axis=1)
# 重命名表头
r.columns = list(data.columns)+[u'聚类类别']

from sklearn.manifold import TSNE
tsne = TSNE()
# 进行降维
tsne.fit_transform(data_zs)
# 转换数据格式
tsne = pd.DataFrame(tsne.embedding_,index=data_zs.index)

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 不同类别用不同颜色和样式绘图
d = tsne[r[u'聚类类别']==0]
plt.plot(d[0],d[1],'r.')
d = tsne[r[u'聚类类别']==1]
plt.plot(d[0],d[1],'go')
d = tsne[r[u'聚类类别']==2]
plt.plot(d[0],d[1],'b*')
plt.show()