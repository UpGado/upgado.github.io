import numpy as np

a = np.array([0,1,2])
b = np.array([4,5,6])
c = np.array([8,9])


def combine(i,j):
    res = []
    for x in i:
        for y in j:
            res.append(np.hstack((x, y)))
    return res

res = combine(a,b)
res = combine(res, c)
print(res)
print(len(res))
'''
for y in b:
    for i in resz:
        resy.append(np.hstack((y, i)))
'''
