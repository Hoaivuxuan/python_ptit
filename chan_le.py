def sum(n):
    cnt=0
    for i in range(1, len(n)):
        cnt=cnt + int(n[i])
    return cnt%10==0
t=int(input())
for i in range(t):
    check=True
    num=input()
    for i in range(1,len(num)):
        if(abs(int(num[i])-int(num[i-1]))!=2):
            check=False
            break
    if(check and sum(num)):
        print("YES")
    else: print("NO")