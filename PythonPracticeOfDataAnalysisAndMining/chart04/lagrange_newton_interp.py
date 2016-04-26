# coding=utf8
# Create by 吴俊 on 2016/4/19

# 代码清单4-1 用拉格朗日法进行插补

# 导入数据分析库pandas
import pandas as pd
# 导入拉格朗日差值函数
from scipy.interpolate import lagrange

# 销量数据路径
inputFile = 'data/catering_sale.xls'
# 输出数据路径
outputFile = 'data/tmp_catering_sales.xls'

# 读入数据
data = pd.read_excel(inputFile)
# 过滤异常值，将其变为空值
data[u'销量'][(data[u'销量']<400)|(data[u'销量']>5000)] = None

# 自定义列向量插值函数
# s为列向量，n为被插值的位置，k为取前后的数据个数，默认为5
def ployinterp_column(s,n,k=5):
    # 取数
    y = s[list(range(n-k,n))+list(range(n+1,n+1+k))]
    # 删除空值
    y = y[y.notnull()]
    # 插值并返回插值结果
    return lagrange(y.index,list(y))(n)

# 逐个元素判断是否需要插值
for i in data.columns:
    for j in range(len(data)):
        # 如果为空值插值
        if (data[i].isnull())[j]:
            data[i][j] = ployinterp_column(data[i],j)
# 输出结果，写入文件
f = open(outputFile,'a')
f.truncate()
f.close()
data.to_excel(outputFile)
