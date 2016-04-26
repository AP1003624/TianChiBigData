# coding=utf8
# Create by 吴俊 on 2016/4/25

# 代码清单5-6 Apriori算法调用代码

from __future__ import print_function
import pandas as pd
# 导入自行编写的Apriori函数
from apriori import *

inputFile = u'data/menu_orders.xls'
outputFile = u'data/tem_apriori_rules.xls'
import os
if os.path.exists(outputFile):
    os.remove(outputFile)
data = pd.read_excel(inputFile,header=None)
print(u'\n转换原始数据至0-1矩阵...')
# 转换0-1矩阵的过渡函数
ct = lambda x: pd.Series(1,index=x[pd.notnull(x)])
# map将函数逐一应用到列表上的每个元素
b = map(ct,data.as_matrix())
# 实现矩阵转换，空值用0填充
data = pd.DataFrame(list(b)).fillna(0)
print(u'\n转换完毕。')
# 删除中间变量b，节省内存
del b

# 最小支持度
support = 0.2
# 最小置信度
confidence = 0.5
# 连接符，默认’---‘，用来区分不同元素，如A---B。需要保证原始表格中不含有该字符
ms = u'---'
# 保存结果
find_rule(data,support,confidence,ms).to_excel(outputFile)