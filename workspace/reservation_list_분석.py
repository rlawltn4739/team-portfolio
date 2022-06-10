import numpy as np
import pandas as  pd
from pandas import DataFrame
from pandas import read_excel
import matplotlib.pylab as plt

df=read_excel("data/reservation.xlsx")
print(df)
print("-"*25)

#전처리
df_r=df["식당"].value_counts()
print(df_r)
