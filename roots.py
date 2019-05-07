import re

def complex_root(a, b):
    s = root([[1,a],[1,a]])[0]
    s[-1] += float(b)**2
    return s

def root(r):
    if len(r) == 1:
        return r
    dev = [0 for i in range(len(r[0]) + len(r[1]) - 1)]

    for i in range(len(r[0])):
        for j in range(len(r[1])):
            dev[i + j] += r[0][i] * r[1][j]
    return root([dev] + r[2:])



v = input().split(',')

comp = []
comv = v[:]
for i in range(len(comv)):
    if 'i' in comv[i]:
        a, b = re.findall("([-\+]\d+)", comv[i])
        print(a,b)
        comp.append(complex_root(float(a), float(b)))
        v.remove(comv[i])


print(comp)
v = [[1,int(i)] for i in v]
v = v+comp

print(root(v))
