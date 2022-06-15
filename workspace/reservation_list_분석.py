import numpy as np
import pandas as  pd
from pandas import DataFrame
from pandas import read_excel
import matplotlib.pylab as plt

df=pd.read_csv("data/reservation.csv")
print(df)
print("-"*25)

df.set_index("레스토랑", inplace=True)
print(df)
