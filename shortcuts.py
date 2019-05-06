import math

def Pythagoras(a,b,c):
    if a == 0:
        a = ((c**2) - (b**2))**(1/2)
    elif c == 0:
        c = ((a**2) + (b**2))**(1/2)
    return (a,b,c)

# def cicle(*rest):
#     cube = 0
#     for i in len(rest):
#         cube += i**3
#     return cube
# def getCom(size):
#     nums = list("0123456789")
#     pat = []
#     for g in range(size):
#         pat.append(0)
#     for h in range(len(pat))
#         for k in nums:
#             pat[-h] = k
#



def limitset(i):
    set = list(str(i))
    ad = 0
    for h in set:
        ad += int(h)**3
    if ad not in added.keys():
        added[ad] = 1
    else:
        if added[ad] > 5:
            added[ad] += 1
            return True
        added[ad] += 1
    limitset(ad)

added = {}
for i in range(1000):
    limitset(i)

answer = 0

for w in sorted(added, key=added.get, reverse=True):
  if added[w] >= 7:
      answer += w
print(answer)
# while True:
#     print("Type the function")
#     fun = (str(input())).lower()
#     if fun.startswith("p"):
#         print("Type a, b, c")
#         a,b,c = eval(input())
#         a,b,c = Pythagoras(a,b,c)
#         print("a: {0}    b: {1}     c: {2}".format(a,b,c))
#     if fun.startswith("g"):
#         getCom()
#     else:
#         break
