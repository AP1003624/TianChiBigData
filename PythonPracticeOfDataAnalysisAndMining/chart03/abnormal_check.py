# coding=utf8
# Create by 吴俊 on 2016/4/18

# 代码清单3-1 餐饮销售数据异常值检测代码 P36

import pandas as pd
# 导入图像库
import matplotlib.pyplot as plt
# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

# 餐饮数据
catering_sale = 'data/catering_sale.xls'
# 读取数据，指定“日期”为索引列
data = pd.read_excel(catering_sale,index_col=u'日期')

# 建立图像
plt.figure()
# 画箱线图，直接使用DataFrame的方法
p = data.boxplot()
# 'fliers'即为异常值标签
x = p['fliers'][0].get_xdata()
y = p['fliers'][0].get_ydata()
# 从小到大排序，该方法直接改变原对象
y.sort()

# 用annotate添加注释
# 其中有些相近的点，注释会出现重叠，难以看清，需要一些技巧来控制
# 以下参数都是进过调试的，需要具体问题具体调试
for i in range(len(x)):
    if i>0:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]),y[i]))
    else:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.08,y[i]))
# 展示箱线图
plt.show()

