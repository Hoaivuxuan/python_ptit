import math
import string
def ucln(a,b):
    bon1=a
    bon2=b
    while(a!=b):
        if(a>b): a-=b
        else: b-=a
    ucln=a
    return ucln
# 
def check(x):
    if x<2 : return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
# 
t=int(input())
for i in range(t):
    a,b=input().split()
    a,b=int(a), int(b)
    point=ucln(a,b)
    sum=0
    for i in str(point):
        sum+=int(i)
    if check(sum): print("YES")
    else: print("NO")
    