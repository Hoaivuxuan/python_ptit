def gcd(a,b):
    while(a>0):
        if a<b:
            a,b=b,a
        a=a%b
    return b
# 
for i in range(int(input())):
    a = int(input())
    b = int(input())
    print(gcd(a,b))
