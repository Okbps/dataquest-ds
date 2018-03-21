import pandas as pd
import numpy as np
from datetime import datetime  
from datetime import timedelta
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

sphist = pd.read_csv("sphist.csv")

sphist['Date'] = pd.to_datetime(arg=sphist['Date'], format='%Y-%m-%d')

sphist.sort_values(by='Date', inplace=True, ascending=False)
sphist.reset_index(inplace=True)

def get_means(df, start, end, cols):
    means = df[(df['Date']>=start) & (df['Date']<=end)][cols].mean()
    return tuple(means[col] for col in cols)

def get_stds(df, start, end, cols):
    stds = df[(df['Date']>=start) & (df['Date']<=end)][cols].std()
    return tuple(stds[col] for col in cols)

new_cols = ['Avg Close 5', 'Avg Close 365', 'Ratio Close 5 365', 'Avg Vol 365', 'Std Vol 365']
df_zeros = np.zeros((sphist.shape[0], len(new_cols)))
sphist[new_cols] = pd.DataFrame(data=df_zeros, index=sphist.index)

for i, row in sphist.iterrows():
    end = sphist.loc[i, 'Date'] - timedelta(days=1)
    start_5 = end - timedelta(days=5)
    start_365 = end - timedelta(days=365)
    
    sphist.loc[i, 'Avg Close 5'] = get_means(sphist, start_5, end, ['Close'])[0]
    sphist.loc[i, 'Avg Close 365'], sphist.loc[i, 'Avg Vol 365'] = get_means(sphist, start_365, end, ['Close', 'Volume'])
    sphist.loc[i, 'Ratio Close 5 365'] = sphist.loc[i, 'Avg Close 5']/sphist.loc[i, 'Avg Close 365']        

for i, row in sphist.iterrows():
    end = sphist.loc[i, 'Date'] - timedelta(days=1)
    start_365 = end - timedelta(days=365)
    
    sphist.loc[i, 'Std Vol 365'] = get_stds(sphist, start_365, end, ['Avg Vol 365'])[0]  
    
    
print(sphist.loc[16584:, ['Date']+new_cols])
print(sphist.loc[:7, ['Date']+new_cols])

sphist = sphist[sphist['Date']>=datetime(year=1951, month=1, day=3)]
sphist.dropna(axis=0, inplace=True)

train = sphist[sphist['Date']<datetime(year=2013, month=1, day=1)]
test = sphist[sphist['Date']>=datetime(year=2013, month=1, day=1)]

lr = LinearRegression()
lr.fit(train[new_cols], train['Close'])
y_hat = lr.predict(test[new_cols])
mae = mean_absolute_error(test['Close'], y_hat)
print("mae:", mae)