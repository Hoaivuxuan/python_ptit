import math
def check(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
# 
T = int(input())
for t in range(T):
    s = input()
    num = 0
    for i in s:
        num += int(i)
    if(check(num)):
        print("YES")
    else: print("NO")
