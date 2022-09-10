import math
# 
def prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0: return False
    return n>1
# 
N=int(input())
arr=input().split()
thisdict={}
for i in arr:
    if prime(int(i)):
        if i in thisdict:
            thisdict[i]+=1
        else: thisdict[i]=1
for one, two in thisdict.items():
    print(str(one) + ' ' + str(two))