import pandas as pd

data = pd.read_csv('data/CRDC2013_14.csv', encoding="Latin-1")

races = ['HI', 'AM', 'AS', 'HP', 'BL', 'WH', 'TR']

def sum_races(row, gender):
    s = 0
    for r in races:
        s = s + row['SCH_ENR_'+r+'_'+gender]
    return s

def sum_m(row):
    return sum_races(row, 'M')

def sum_f(row):
    return sum_races(row, 'F')

data['TOT_ENR_M'] = data.apply(sum_m, axis=1)
data['TOT_ENR_F'] = data.apply(sum_f, axis=1)

data['total_enrollment'] = data['TOT_ENR_M'] + data['TOT_ENR_F']

all_enrollment = data['TOT_ENR_M'].sum()

print('percentage of total:')
for g in ['M', 'F']:
    for r in races:
        col = 'SCH_ENR_'+r+'_'+g
        print(col + ': ' + str(data[col].sum()/all_enrollment))
