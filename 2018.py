from math import factorial as factorial

def yearfactor(num):
     upper = int((num)**(1/2))

     for i in range(1, upper+1):
         if num%i == 0:
             if i == 2018 or num/i == 2018:
                 return num


while True:
    num = "30000"
    for i in range(1,5):
        comb = factorial(i)

    break
