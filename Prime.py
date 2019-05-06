

for a in range(10000, 20001):

    num = a
    root = int(num**(1/2)+1)
    row = False

    for i in range(2, root + 1):
        if num % i == 0:
            break
        if i == root:
            print(a)
