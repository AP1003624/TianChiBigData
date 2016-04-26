# coding=utf8
# Create by 吴俊 on 2016/4/19

import pandas as pd

inputFile = 'data/principal_component.xls'
outFile = 'data/temp_principal_component.xls'

data = pd.read_excel(inputFile,header=None)
from sklearn.decomposition import PCA

pca = PCA()
pca.fit(data)
# 返回模型的各个特征向量
print(u'模型的各个特征向量:')
print(pca.components_)
# 返回各个成分各自的方差百分比
print(u'各个成分各自的方差百分比')
print(pca.explained_variance_ratio_)

pca = PCA(3)
pca.fit(data)
# 用它来降低维度
low_d = pca.transform(data)
# 保存结果
f = open(outFile)
f.truncate()
f.close()
pd.DataFrame(low_d).to_excel(outFile)
# 必要时可以用inverse_transform()函数来复原数据
pca.inverse_transform(low_d)