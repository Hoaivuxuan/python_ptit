# 
t=int(input())
while t>0:
    n,x,m=input().split()
    n,x,m=float(n), float(x), float(m)
    days=0
    while(n<m):
        n=n+n*(x/100.0)
        days+=1
    print(days)
    t-=1