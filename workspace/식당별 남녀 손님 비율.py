from pandas import DataFrame, read_excel
from pandas import ExcelFile
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
'''
xls = ExcelFile('data/reservation.xlsx')
#print(xls)
df= xls.parse(xls.sheet_names[0])
print(df)
df.to_csv('data/reservation.csv')
print('--------------------------')

df = pd.read_csv('data/reservation.csv')
print(df)
print('--------------------------')
'''
restaurant_data = {
    "연령": [30,32,50,36,21,41,48,41,57,44,30,32,50,36,21,41,48,41,57,44,27],
    "성별": ["여자", "남자","남자", "여자", "남자", "남자", "여자", "여자","남자", "여자","남자", "남자","남자", "남자", "여자", "여자", "여자", "여자","남자", "여자","남자"],
    "식당": ["삼청각", "정식당","곰바위", "정식당", "텅앤그루브", "곰바위", "삼청각", "삼청각","곰바위", "텅앤그루브","삼청각", "암소서울","삼청각", "곰바위", "암소서울", "곰바위", "곰바위", "텅앤그루브","곰바위", "암소서울","정식당"],
    "인원": [30,32,50,36,21,41,48,41,57,44,32,50,36,21,41,48,41,57,44,10,5]
}
df = DataFrame(restaurant_data)
print(df)
print('-'*20)

gender= df.filter(['성별','식당'])
print(gender)
print('-'*20)
gender['성별'][gender['성별']=='남자'] = 1
gender['성별'][gender['성별']=='여자'] = 0
print(gender)
print('-'*20)

#df1 = df1.rename(index=df['식당']).drop('식당', axis=1)
#print(df1)
#print('--------------------------')

gender_groups=gender.groupby('식당').mean()
print(gender_groups)
print('-'*20)

gender_groups.rename(columns={'성별':'남성비율'}, inplace=True)
print(gender_groups)
print('-'*20)

gender_groups['여성비율'] = 1 - gender_groups['남성비율']
print(gender_groups)
print('-'*20)

gender_groups.plot.bar(rot=0)
plt.rcParams['font.family']='batang'
plt.xlabel('식당명')
plt.ylabel('남녀 고객 비율')
plt.grid()
plt.ylim(0,1)
plt.rcParams['figure.figsize'] = (6,4)
