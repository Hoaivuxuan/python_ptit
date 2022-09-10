# from cmath import sqrt
import math
box = ['2', '3', '5', '7']
def prime(a):
    for i in range(2, int(math.sqrt(a))+1):
        if a%i==0:
            return False
    return a>1
# 
t=int(input())
for i in range(t):
    number=input()
    check=True
    for i in range(0, len(number)):
        if prime(i):
            if number[i] not in box:
                check=False
                break
        else:
            if number[i] in box:
                check= False
                break
    if check:
        print("YES")
    else:
        print("NO")