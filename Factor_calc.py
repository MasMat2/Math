




while True:

    try:
        num = int(input())
    except:
        break

    upper = int((num)**(1/2))
    factors = []

    for i in range(1, upper+1):
        if num%i == 0:
            factors.append(i)
            factors.append(int(num/i))

    factors.sort()

    print(factors)
