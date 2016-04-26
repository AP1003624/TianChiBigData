# coding=utf8
# Create by 吴俊 on 2016/4/18

# 代码清单3-3 菜品盈利帕累托图代码

from __future__ import print_function
import pandas as pd

# 初始化参数
# 餐饮菜品盈利数据
dish_profit = 'data/catering_dish_profit.xls'
data = pd.read_excel(dish_profit,index_col=u'菜品名')
# print(data)
data = data[u'盈利'].copy()
data.sort(ascending = False)
# print(data)

# 导入图像库
import matplotlib.pyplot as plt
# 用来正常显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False
plt.figure()
data.plot(kind='bar')
plt.ylabel(u'盈利(元)')
p = 1.0*data.cumsum()/data.sum()
p.plot(color='r',secondary_y=True,style='-o',linewidth=2)
# 添加注释，即85%处的标记。这里包括了指定箭头样式
plt.annotate(format(p[6],'.4%'),xy=(6,p[6]),xytext=(6*0.9,p[6]*0.9),arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))
plt.ylabel(u'盈利(比例)')
plt.show()
