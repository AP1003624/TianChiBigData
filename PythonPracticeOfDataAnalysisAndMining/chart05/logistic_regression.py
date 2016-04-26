# coding=utf8
# Create by 吴俊 on 2016/4/23

# 代码清单5-1 逻辑回归代码

import pandas as pd
# 参数初始化
fileName = 'data/bankloan.xls'
data = pd.read_excel(fileName)
x = data.iloc[:,:8].as_matrix()
y = data.iloc[:,8].as_matrix()

# 逻辑回归模型
from sklearn.linear_model import LogisticRegression as LR
# 随机逻辑回归模型
from sklearn.linear_model import RandomizedLogisticRegression as RLR
# 建立随机逻辑回归模型，筛选变量
rlr = RLR()
# 训练模型
rlr.fit(x,y)
# 获取特筛选结果，也可以通过.score_方法获取各个特征的分数
rlr.get_support()
print(u'通过随机逻辑回归模型筛选特征结束。')
print(u'有效特征为 %s' %'.'.join(data.columns[rlr.get_support()]))
# 筛选好特征
x = data[data.columns[rlr.get_support()]].as_matrix()

# 建立逻辑回归模型
lr = LR()
# 用筛选后的特征数据来训练模型
lr.fit(x,y)
print(u'逻辑回归模型训练结束。')
# 给出模型的平均正确率，本例为81.48
print(u'模型的平均正确率为 %s' %lr.score(x,y))