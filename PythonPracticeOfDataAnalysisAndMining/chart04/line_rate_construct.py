# coding=utf8
# Create by 吴俊 on 2016/4/19

# 代码清单4-4 线损率属性构造

import pandas as pd

inputFile = 'data/electricity_data.xls'
outFile = 'data/temp_electricity_data.xls'

data = pd.read_excel(inputFile)
data[u'线损率'] = (data[u'供入电量']-data[u'供出电量'])/data[u'供出电量']
data.to_excel(outFile,index = False)
