# coding=utf8
# Create by 吴俊 on 2016/4/18

#代码清单3-4 餐饮销售数据相关性分析
from __future__ import print_function
import pandas as pd
# 餐饮数据，含其他属性
catering_sale = 'data/catering_sale_all.xls'
# 读取数据，指定“日期”列为索引列
data = pd.read_excel(catering_sale,index_col=u'日期')
# 相关系数矩阵，即给出了任意两款菜式之间的相关系数
print(data.corr())
# 只显示“百合酱蒸凤爪”与其他菜式的相关系数
print(data.corr()[u'百合酱蒸凤爪'])
# 计算“百合酱蒸凤爪”与“翡翠蒸香茜饺”的相关系数
# print(data[u'百合酱蒸凤爪'].corr(data[u'翡翠蒸香茜饺']))
# print(data.corr()[u'百合酱蒸凤爪'][u'翡翠蒸香茜饺'])