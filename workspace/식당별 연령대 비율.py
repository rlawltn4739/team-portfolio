from pandas import DataFrame, read_excel
from pandas import ExcelFile
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

restaurant_data = {
    "연령": [30,32,50,36,25,41,38,41,32,54,30,32,50,36,21,41,48,41,28,44],
    "성별": ["남자", "여자","여자", "남자", "남자", "여자", "여자", "여자","남자", "여자","남자", "남자","남자", "남자", "여자", "여자", "여자", "여자","남자", "여자"],
    "식당": ["삼청각", "정식당","곰바위", "암소서울", "텅앤그루브", "곰바위", "정식당", "삼청각","곰바위", "텅앤그루브","삼청각", "암소서울","삼청각", "곰바위", "암소서울", "곰바위", "곰바위", "텅앤그루브","곰바위", "암소서울"],
    "인원": [30,32,50,36,21,41,48,41,57,44,32,50,36,21,41,48,41,57,44,10]
}
df = DataFrame(restaurant_data)
print(df)
print('-'*20)

age= df.filter(['연령','식당'])
print(age)
print('-'*20)
print(age['연령'].dtypes)

def age_categorize(age) :
    age = (age // 10) * 10
    return age

age['연령대'] = age_categorize(age['연령']) 
print(age)
print('-'*20)

age_result = age.groupby('식당').mean()
print(age_result)
print('-'*20)

age_result.plot.bar(rot=0)
plt.xlabel('식당명')
plt.ylabel('연령대별 고객 비율')
plt.grid()
plt.ylim(10,50)
plt.rcParams['figure.figsize'] = (6,4)
plt.rcParams['font.family']='batang'