import read
from collections import Counter

df = read.load_data()

df['headline'].fillna('')

s = ''

for i in range(len(df)):
    s += str(df['headline'].loc[i])
    s += ' '
    
s = s.lower()
words = s.split(sep=' ')    
counter = Counter(words)
print(counter.most_common(100))