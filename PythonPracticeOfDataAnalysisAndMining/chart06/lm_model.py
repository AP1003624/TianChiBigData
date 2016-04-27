# coding=utf8
# Create by 吴俊 on 2016/4/27

# 代码清单6-2 原始数据分为训练数据测试数据
import pandas as pd
# 导入随机函数shuffle，用来打散数据
from random import shuffle

dataFile = 'data/model.xls'
# 数据的前三列为特征，第四列是标签
data = pd.read_excel(dataFile)
# 将表格转换为矩阵
data = data.as_matrix()
# 随机打散数据
shuffle(data)

# 设置训练数据比例
p = 0.8
# 前80%为训练集
train = data[:int(len(data)*p),:]
# 后20%为测试集
test = data[int(len(data)*p):,:]

# 代码清单6-3 构建LM神经网络模型代码
# 导入神经网络初始化函数
from keras.models import Sequential
# 导入神经网络层函数、激活函数
from keras.layers.core import Dense,Activation

# 构建的神经网络模型存储路径
netFile = u'model/net.model'

# 建立神经网络
net = Sequential()
# 添加输入层（3节点）到隐藏层（10节点）的连接
net.add(Dense(10,input_dim=3))
# 隐藏层使用relu激活函数
net.add(Activation('relu'))
# 添加隐藏层（10节点）到输出层（1节点）的连接
net.add(Dense(1))
# # # 输出层使用sigmoid激活函数
net.add(Activation('sigmoid'))
# 编译模型，用adam求解
net.compile(loss='binary_crossentropy',optimizer='adam',class_mode='binary')
# 训练模型，循环1000次
net.fit(train[:,:3],train[:,3],nb_epoch=1000,batch_size=1)
# 保存模型
net.save_weights(netFile)

# 这里要提醒的是，Keras用predict给出预测概率，predict_classes才是给出预测类型，
# 而且两者的预测结果都是n*1维数组，而不是通常的1*n
predict_result = net.predict_classes(train[:,:3]).reshape(len(train))

# 导入自行编写的混淆矩阵可视化函数
from cm_plot import *
cm_plot(train[:,3],predict_result).show()

# 代码清单6-5 绘制决策树模型的ROC曲线
# 导入ROC曲线函数
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt

# 预测结果变形
predict_result = net.predict(test[:,:3]).reshape(len(test))
fpr,tpr,thresholds = roc_curve(test[:,3],predict_result,pos_label=1)
# 作出ROC曲线
plt.plot(fpr,tpr,linewidth=2,label='ROC of LM')
# 坐标轴标签
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
# 边界范围
plt.xlim(0,1.05)
plt.ylim(0,1.05)
# 图例
plt.legend(loc=4)
plt.show()
