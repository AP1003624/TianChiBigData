# coding=utf8
# Create by 吴俊 on 2016/4/27

# 代码清单6-1 拉格朗日插值代码

import pandas as pd
# 导入拉格朗日插值函数
from scipy.interpolate import lagrange

# 输入数据路径，需要使用Excel格式
inputFile = u'data/missing_data.xls'
# 输出数据路径，需要使用Excel格式
outputFile = u'data/tmp_missing_data_processed.xls'
# 读入数据
data = pd.read_excel(inputFile,header=0)
# 获取除第一列以外其他数据
data_num = data.loc[:,[u'用户A',u'用户B',u'用户C']]
# 自定义列向量插值函数
# s为列向量，n为被插值的位置，k为取前后的数据个数，默认为5
def ployinterp_colums(s,n,k=5):
    # 取数
    y = s[list(range(n-k,n))+list(range(n+1,n+1+k))]
    # 剔除空值
    y = y[y.notnull()]
    # 插值并返回插值结果
    return lagrange(y.index,list(y))(n)

# 逐个元素判断是否需要插值
for i in data_num.columns:
    for j in range(len(data)):
        # 如果为空即插值
        if (data_num[i].isnull())[j]:
            data_num[i][j] = ployinterp_colums(data_num[i],j)
# 输出结果
data = pd.concat([data[u'日期'],data_num],axis=1)
data.columns = list(data.columns)
data.to_excel(outputFile,index=False)