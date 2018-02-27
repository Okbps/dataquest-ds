import pandas as pd

data = pd.read_csv('data/CRDC2013_14.csv', encoding="Latin-1")
print(data['JJ'].value_counts())
print(data['SCH_STATUS_MAGNET'].value_counts())

pivot_jj = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="JJ", aggfunc="sum")
print(pivot_jj)

pivot_magnet = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="SCH_STATUS_MAGNET", aggfunc="sum")
print(pivot_magnet)