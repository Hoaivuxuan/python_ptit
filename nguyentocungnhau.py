def ucln(a,b):
    while(a>0):
        if(a<b):
            a,b=b,a
        a%=b
    return b
# 
N,K=map(int, input().split())
cnt=0
for i in range(10**(K-1), 10**(K)):
    if(ucln(i, N)==1):
        if(cnt==10):
            cnt=0
            print()
        print(i, end=' ')
        cnt+=1