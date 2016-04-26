# coding=utf8
# Create by 吴俊 on 2016/4/19

# 代码清单4-2 数据规范化代码

import pandas as pd
import numpy as np

# 参数初始化
dataFile = 'data/normalization_data.xls'
# 读取数据
data = pd.read_excel(dataFile,header=None)
print(u'原始数据')
print(data)
# 最小-最大规范化
print(u'最小-最大规范化')
print(((data-data.min())/(data.max()-data.min())))
# 零-均值规范化
print(u'零-均值规范化')
print((data-data.mean())/data.std())
# 小数定标规范化
print(u'小数定标规范化')
print((data/10**np.ceil(np.log10(data.abs().max()))))

