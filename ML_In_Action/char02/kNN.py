# coding=utf8
# Create by 吴俊 on 2016/3/31

from numpy import *
import operator

def createDateSet():
    group = array([[1.0,1.1],[1.0,1.0],[0.0,0.0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels


def classify0(inX, dataSet ,lables, k) :
    '''
    程序清单2-1 K-近邻算法
    :param inX: 用于分类的输入向量
    :param dataSet: 输入的训练样本集
    :param lables: 标签向量
    :param k: 用于选择最近邻居的数目
    :return: 前K个点出现出现频率最高的类别
    '''
    dataSetSize = dataSet.shape[0]
    # 距离计算
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDifMat  = diffMat**2
    sqDistances = sqDifMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlable = lables[sortedDistIndicies[i]]
        # 选择距离最小的K个点
        classCount[voteIlable] = classCount.get(voteIlable,0)+1
    # 排序
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def file2matrix(fileName):
    '''
    程序清单2-2 将文本记录转换为NumPy的解析程序
    :param fileName: 待处理数据的文件名字符串
    :return: 训练样本矩阵和类标签向量
    '''
    fr = open(fileName)
    arrayOLines = fr.readlines()
    # 得到文件行数
    numberOLines = len(arrayOLines)
    # 创建返回的Numpy矩阵
    returnMat = zeros((numberOLines,3))
    classLabelVector = []
    index = 0
    # 解析文件数据到列表
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

def autoNorm(dataSet):
    '''
    程序清单2-3 归一化特征值
    :param dataSet:
    :return:
    '''
    # 0：按列处理，1：按行处理
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet-tile(minVals,(m,1))
    # 特征值相除
    normDataSet = normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges,minVals

def datingClassTest():
    '''
    程序清单2-4 分类器针对约会网站的测试代码
    :return: 计算错误率
    '''
    hoRatio = 0.10
    datingDataMat,datingLabels = file2matrix('data/datingTestSet2.txt')
    normMat,ranges,minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print(u'the classifierResult came back with: %s , the real answer is : %s' %(classifierResult,datingLabels[i]))
        if(classifierResult!=datingLabels[i]):
            errorCount +=1.0
    print(u'the total error rate is: %f' %(errorCount/float(numTestVecs)))

def classifyPerson():
    '''
    程序清单2-5 约会网站预测函数
    :return:预测值
    '''
    resultList = ['not at all','in small doses','in large doses']
    percentTats = float(raw_input(u"percentage of time spent playing video games?"))
    ffMiles = float(raw_input(u"frequent flier miles earned per years?"))
    iceCream = float(raw_input(u"liters of ice cream consumed per years?"))
    datingDataMat,datingLabels = file2matrix('data/datingTestSet2.txt')
    normMat,ranges,minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles,percentTats,iceCream])
    classifierResult = classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
    print(u"You will probably like this person: %s" %resultList[classifierResult-1])

if __name__ == '__main__':
    # 约会网站预测函数
    classifyPerson()

    # 分类器针对约会网站的测试代码
    # datingClassTest()

    # # 程序清单2-1
    # group,lables = createDateSet()
    # classify=classify0([0,0,],group,lables,3)
    # print(classify)

    # 程序清单2-2
    # datingDataMat,datingLabels = file2matrix('data/datingTestSet2.txt')
    # print(datingDataMat)
    # print(datingLabels[0:20])

    # 使用Matplotlib创建散点图
    # import matplotlib.pyplot as plt
    # plt.rcParams['font.sans-serif'] = 'SimHei'
    # plt.rcParams['axes.unicode_minus'] = False
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
    # plt.show()

    # 程序清单2-3
    # normMat,ranges,minVals = autoNorm(datingDataMat)
    # print(normMat)
    # print(ranges)
    # print(minVals)


