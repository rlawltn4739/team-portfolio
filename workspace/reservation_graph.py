import numpy as np
import pandas as  pd
from pandas import DataFrame
from pandas import read_excel
import matplotlib.pylab as plt

df=read_excel("data/guest_list.xlsx")
print(df)
print("-"*25)

df.set_index("식당", inplace=True)
print(df)
print(df.iloc[:,:1])


# df_r=df['식당'].value_counts()
# print(df_r)

# plt.rcParams["font.family"]="Malgun Gothic"
# plt.rcParams["font.size"]=15
# plt.rcParams["figure.figsize"]=(15,7)
# df_r.plot.bar(color=["#485E57","#e9bd7c"], alpha=0.7)
# plt.grid()
# plt.title("지난 달 다같이를 통해 가장 많이 예약된 식당",size=25)
# plt.show()