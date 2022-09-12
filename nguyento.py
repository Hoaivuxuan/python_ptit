import math 
# 
def UCLN(a,b):
    if b==0:
        return a
    return UCLN(b,a%b)
# 
def check_nt(n):
    if n<2: return 0
    else : 
        for i in range(2, int(math.sqrt(n))+1):
            if n%i==0 : return 0
        return 1
# 
def count_val(n):
    cnt=0
    for i in range(1,n):
        if UCLN(i,n)==1:
            cnt+=1
    return cnt
# 
t=int(input())
while t>0:
    n=int(input())
    box = count_val(n)
    if check_nt(box) : print("YES")
    else : print("NO")
    t-=1