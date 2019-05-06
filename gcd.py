def gcd(a,b):
    if 0 in (a,b):
        return "Zero error"
    elif a > b:
        big = a
        small = b
    else:
        big = b
        small = a

    while 1:
        c = big % small
        if c == 0:
            return small
        big = small
        small = c
