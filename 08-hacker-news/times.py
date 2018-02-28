import read
from dateutil import parser

def get_hours(raw):
    time = parser.parse(raw)
    return time.hour

df = read.load_data()

df['hours'] = df['submission_time'].apply(get_hours)

print(df['hours'].value_counts()[:100])