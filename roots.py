

def root(r):
    if len(r) == 1:
        return r
    dev = [0 for i in range(len(r[0]) + 1)]

    for i in range(len(r[0])):
        for j in range(2):
            dev[i + j] += r[0][i] * r[1][j]
    return root([dev] + r[2:])


v = input().split(',')
v = [[1,int(i)] for i in v]
a = ''
for i in v:
    if  i[0] == 1:
        if i[1]<0:
            a += f'(x - {-i[1]})'
        else:
            a += f'(x + {i[1]})'


print(a)
print(root(v))
