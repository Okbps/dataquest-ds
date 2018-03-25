def linDictSearch(l, item):
    for row in l:
        for key, value in row.items():
            if value==item:
                return row

def biSearch(l, item, col):
    if len(l) == 0:
        return float('nan')
    else:
        midpoint = len(l)//2
        if l[midpoint][2] == item:
            return l[midpoint]
        else:
            if item < l[midpoint][2]:
                return biSearch(l[:midpoint], item, col)
            else:
                return biSearch(l[midpoint+1:], item, col)
