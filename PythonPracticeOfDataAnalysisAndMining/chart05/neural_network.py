# coding=utf8
# Create by 吴俊 on 2016/4/23

# 代码清单5-3 神经网络算法预测销量高低

import pandas as pd

# 参数初始化
inputFile = 'data/sales_data.xls'
data = pd.read_excel(inputFile,index_col=u'序号')

# 数据是类别标签，要将它转换为数据
# 用1来表示“好”、“是”、“高”这三个属性，用-1来表示“坏”、“否”、“低”
data[data == u'是'] = 1
data[data == u'好'] = 1
data[data == u'高'] = 1
data[data != 1] = -1
x = data.iloc[:,:3].as_matrix().astype(int)
y = data.iloc[:,3].as_matrix().astype(int)

from keras.models import Sequential
from keras.layers.core import Dense,Activation

# 建立模型
model = Sequential()
# 3个输入的，10个隐藏点
model.add(Dense(10,input_dim=3))
# 用relu函数作为输入函数，能够大幅度提供准确度
model.add(Activation('relu'))
# 10个隐藏节点，1个输出节点(第一层指定输入输出后其他层不用再指定输入层）
model.add(Dense(1))
# 由于是0-1输出，用sigmoid函数作为激活函数
model.add(Activation('sigmoid'))

# 编译模型。由于我们做的是二元分类，所以我们指定损失函数为binary_crossentropy，以及模式为binary
# 另外常见的损失函数还有mean_squared_error、categorical_crossentropy等，请阅读帮助文件
# 求解方法我们指定用adam，还有sgd，rmsprop等
model.compile(loss='binary_crossentropy',optimizer='adam',class_mode='binary')
# 训练模型，学习1000次
model.fit(x,y,nb_epoch=1000,batch_size=10)
# 分类预测
yp = model.predict_classes(x).reshape(len(y))



# 混淆矩阵可视化函数
def cm_plot(y, yp):
  '''
  混淆矩阵可视化函数
  '''
  from sklearn.metrics import confusion_matrix #导入混淆矩阵函数

  cm = confusion_matrix(y, yp) #混淆矩阵

  import matplotlib.pyplot as plt #导入作图库
  plt.matshow(cm, cmap=plt.cm.Greens) #画混淆矩阵图，配色风格使用cm.Greens，更多风格请参考官网。
  plt.colorbar() #颜色标签

  for x in range(len(cm)): #数据标签
    for y in range(len(cm)):
      plt.annotate(cm[x,y], xy=(x, y), horizontalalignment='center', verticalalignment='center')

  plt.ylabel('True label') #坐标轴标签
  plt.xlabel('Predicted label') #坐标轴标签
  return plt


# 显示混淆矩阵可视化结果
cm_plot(y,yp).show()


