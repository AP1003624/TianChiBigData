# coding=utf8
# Create by 吴俊 on 2016/4/18

import pandas as pd
import numpy as np


# 计算两个列向量的相关系数，采用Spearman方法，默认的是person
# 生成样本D，一行为1~7，一行为2~8
# D = pd.DataFrame([range(1,8),range(2,9)])
# 计算相关系数矩阵
# spearmanCorr = D.corr(method='spearman')
# print(spearmanCorr)
# 提取第一行
# 提取第一列：D[0]
# S1 = D.loc[0]
# print(S1)
# 提取第二行
# 提取第二列：D[1]
# S2 = D.loc[1]
# print(S2)
# 计算S1、S2的相关系数
# S12 = S1.corr(S2,method='pearson')
# print(S12)


# 产生6*5随机矩阵
# D = pd.DataFrame(np.random.randn(6,5))


# 计算6*5随机矩阵的协方差
# # 计算协方差
# cov = D.cov()
# print(cov)
# # 计算第一列和第二列的协方差
# cov12 = D[0].cov(D[1])
# print(cov12)

# 计算6*5随机矩阵的偏度（三阶矩）/峰度（四阶矩）
# 偏度（三阶矩）
# skew = D.skew()
# print(skew)
# # 峰度（四阶矩）
# kurt = D.kurt()
# print(kurt)

# 给出6*5随机矩阵的describe
# print(D.describe())


# D = pd.DataFrame(range(0,20))
# print(u'给出前N项和:')
# print(D.cumsum())
# print(u'依次对相邻两项求和：')
# print(pd.rolling_sum(D,2))

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(7,5))
# 在区间（0<=x<=2pi）绘制一条蓝色的正弦虚线，并在每个坐标点表示五角星
# # X坐标输入
# x = np.linspace(0,2*np.pi,50)
# # 计算对应X的正弦值
# y = np.sin(x)
# # 控制图形格式为蓝色带星虚线，显示正弦曲线
# plt.plot(x,y,'bp--')
# plt.show()


# 通过相邻[15,30,45,10]画饼图，注上标签，并将第2部分分离出来
# 定义标签
# labels = ['Frogs','Hogs','Dog','Logs']
# # 每一块的比例
# sizes = [15,30,45,10]
# # 每一块的颜色
# colors = ['yellowgreen','gold','lightskyblue','lightcoral']
# # 突出显示，这里仅仅突出显示第二块
# explode = (0,0.1,0,0)
# plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)
# # 显示为圆，避免压缩为椭圆
# plt.axis('equal')
# # 保存图片，jpg格式会出错
# # plt.savefig('l.png')
# plt.show()
