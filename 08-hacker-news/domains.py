import read
import re

df = read.load_data()

def remove_subdom(url):
    if type(url) is str and url.count('.') > 1:
        url = re.sub('^[a-zA-Z0-9_-]*\.', '', url)
    return url

df['url'] = df['url'].apply(remove_subdom)

domains = df['url'].value_counts()[:100]

for name, row in domains.items():
    print("{0}: {1}".format(name, row))