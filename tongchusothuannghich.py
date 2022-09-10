def check(n):
    m=str(n)
    if len(m)>1 and m==m[::-1]:
        return 'YES'
    else: 
        return 'NO'
# 
t=int(input())
for i in range(t):
    number=input()
    cnt=0
    for k in number:
        cnt+=int(k)
    print(check(cnt))