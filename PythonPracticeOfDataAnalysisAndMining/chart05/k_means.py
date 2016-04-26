# coding=utf8
# Create by 吴俊 on 2016/4/23

# 代码清单5-4 使用K-Means聚类算法代码

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
print(r)

# 详细输出原始数据及其类别
# 输出每个样本对应的类别
r = pd.concat([data,pd.Series(model.labels_,index=data.index)],axis=1)
# 重命名表头
r.columns = list(data.columns)+[u'聚类类别']
r.to_excel(outFile)

# 绘制聚类后的概率密度图
def density_plot(data,title):
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure()
    # 逐列绘制
    for i in range(len(data.iloc[0])):
        (data.iloc[:,i]).plot(kind='kde',label=data.columns[i],linewidth=2)
    plt.ylabel(u'密度')
    plt.xlabel(u'人数')
    plt.title(u'聚类类别%s各属性的密度曲线' %title)
    plt.legend
    return plt

def density_plot(data):
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    p = data.plot(kind='kde',linewidth=2,subplots=True,sharex=False)
    [p[i].set_ylabel(u'密度') for i in range(K)]
    plt.legend()
    return plt

# 概率密度图文件名前缀
pic_out = u'data/pd_'
import fnmatch
for file in os.listdir('data'):
    if fnmatch.fnmatchcase(file,'pd_*.png'):
        os.remove(u'data/'+file)

for i in range(K):
    density_plot(data[r[u'聚类类别']==i]).savefig(u'%s%s.png' %(pic_out,i))
