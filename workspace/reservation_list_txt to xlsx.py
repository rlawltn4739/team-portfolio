import pandas as  pd

df=pd.read_csv("data/reservation.txt", sep="/", encoding="euc-kr")
print(df)
df.to_excel("reservation.xlsx", index=True)