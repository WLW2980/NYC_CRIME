import pandas as pd
import numpy as np

inputfile='nypd.csv'
outputfile='年犯罪数据.csv'

data=pd.read_csv(inputfile)
#
#
a=data['CMPLNT_FR_DT']
a=a.dropna()
a.to_csv(outputfile)

# print(a['VIC_AGE_GROUP'].unique())
# print(a['SUSP_AGE_GROUP'].unique())
#
#
# a.loc[a.SUSP_AGE_GROUP=='UNKNOWN','SUSP_AGE_GROUP']=None
# a.loc[a.SUSP_AGE_GROUP=='2016','SUSP_AGE_GROUP']=None
# a.loc[a.SUSP_AGE_GROUP=='915','SUSP_AGE_GROUP']=None
# a.loc[a.SUSP_AGE_GROUP=='942','SUSP_AGE_GROUP']=None
# a.loc[a.SUSP_AGE_GROUP=='926','SUSP_AGE_GROUP']=None
# a.loc[a.SUSP_AGE_GROUP=='<18','SUSP_AGE_GROUP']=9
# a.loc[a.SUSP_AGE_GROUP=='18-24','SUSP_AGE_GROUP']=21
# a.loc[a.SUSP_AGE_GROUP=='25-44','SUSP_AGE_GROUP']=35
# a.loc[a.SUSP_AGE_GROUP=='45-64','SUSP_AGE_GROUP']=55
# a.loc[a.SUSP_AGE_GROUP=='65+','SUSP_AGE_GROUP']=75
#
# a.loc[a.VIC_AGE_GROUP=='UNKNOWN','VIC_AGE_GROUP']=None
# a.loc[a.VIC_AGE_GROUP=='912','VIC_AGE_GROUP']=None
# a.loc[a.VIC_AGE_GROUP=='-980','VIC_AGE_GROUP']=None
# a.loc[a.VIC_AGE_GROUP=='929','VIC_AGE_GROUP']=None
# a.loc[a.VIC_AGE_GROUP=='808','VIC_AGE_GROUP']=None
# a.loc[a.VIC_AGE_GROUP=='-978','VIC_AGE_GROUP']=None
# a.loc[a.VIC_AGE_GROUP=='<18','VIC_AGE_GROUP']=9
# a.loc[a.VIC_AGE_GROUP=='18-24','VIC_AGE_GROUP']=21
# a.loc[a.VIC_AGE_GROUP=='25-44','VIC_AGE_GROUP']=35
# a.loc[a.VIC_AGE_GROUP=='45-64','VIC_AGE_GROUP']=55
# a.loc[a.VIC_AGE_GROUP=='65+','VIC_AGE_GROUP']=75
# print(a['VIC_AGE_GROUP'].unique())
# print(a['SUSP_AGE_GROUP'].unique())
#
# print(a.isnull().sum())
# a=a.dropna()
# print(a.isnull().sum())
# a.to_csv(outputfile)