# coding=utf8
# Create by 吴俊 on 2016/4/18

# 读入数据，查看数据的基本统计情况 P35
# 代码清单3-2 餐饮销量数据统计分析代码

from __future__ import print_function
import pandas as pd

# 餐饮数据
catering_sale = 'data/catering_sale.xls'
# 读取数据，指定'日期'列为索引
data = pd.read_excel(catering_sale,index_col=u'日期')
# print(data.describe())
# 过滤异常数据，过滤条件需要用()
data = data[(data[u'销量']>400) & (data[u'销量']<5000)]
# 保存基本统计量
statistics = data.describe()
print(statistics)
# print(statistics)
# 极差
statistics.loc['range'] = statistics.loc['max'] - statistics.loc['min']
# 变异系数
statistics.loc['var'] = statistics.loc['std'] / statistics.loc['mean']
# 四分位数间距
statistics.loc['dis'] = statistics.loc['75%'] - statistics.loc['25%']
print(statistics)