# import numpy as np
#
def check(number):
    for i in number:
        if(i!='4' and i!='7'): return False
    return True
# 
t=int(input())
while t>0:
    number=str(input())
    if(check(number)): print("YES")
    else: print("NO")
    t=t-1