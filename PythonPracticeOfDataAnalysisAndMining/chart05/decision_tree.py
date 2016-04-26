# coding=utf8
# Create by 吴俊 on 2016/4/23

# 代码清单5-2 决策树算法预测销量高低代码
import pandas as pd

# 参数初始化
fileName = u'data/sales_data.xls'
data = pd.read_excel(fileName,index_col=u'序号')

# 数据是类别标签，要将它转换为数据
# 用1来表示“好”、“是”、“高”这三个属性，用-1来表示“坏”、“否”、“低”
data[data == u'好'] = 1
data[data == u'是'] = 1
data[data == u'高'] = 1
data[data != 1] = -1
x = data.iloc[:,:3].as_matrix().astype(int)
y = data.iloc[:,3].as_matrix().astype(int)

from sklearn.tree import DecisionTreeClassifier as DTC
# 建立决策树模型，基于信息熵
dtc = DTC(criterion="entropy")
# 训练模型
dtc.fit(x,y)

# 导入相关函数，可视化决策树。
# 导出的结果是一个dot文件，需要安装Graphviz才能将它转换为pdf或png等格式。
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
with open(u'data/tree.dot','w') as f:
    f.truncate()
    f = export_graphviz(dtc,feature_names=x.columns,out_file=f)  # x.columns这里有问题