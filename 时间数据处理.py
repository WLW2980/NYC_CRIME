import pandas as pd
import time
import datetime
import email.utils as eutils
inputfile='xiaqu.csv'
outputfile='xiaqu.csv'
data=pd.read_csv(inputfile)
# print(data['CMPLNT_TO_TM'][9])
# print(data.loc[9]['CMPLNT_TO_TM'])
#去除空值的行
data=data.dropna()
#去除time为24：00：00
# data.loc[:][data.CMPLNT_TO_TM=='24:00:00']=None
# print( data['CMPLNT_TO_TM'].isnull().sum())
# data=data.dropna()
# #合并date 和time
# data['starttime']=data['CMPLNT_FR_DT']+' '+data['CMPLNT_FR_TM']
# data['endtime']=data['CMPLNT_TO_DT']+' '+data['CMPLNT_TO_TM']
#
# #转变成时间类型
# data['starttime']=pd.to_datetime(data['starttime'],format='%Y/%m/%d %H:%M:%S')
# data['endtime']=pd.to_datetime( data['endtime'],format='%Y/%m/%d %H:%M:%S')
# #定义犯罪时间间隔
# data['interval']=(data['starttime']-data['endtime']).apply(lambda x:x.days)
# #去除时间间隔大于0
# data.loc[data.interval>0,'starttime']=None
# data=data.dropna()
#输出
data.to_csv(outputfile)