a,k,n=input().split()
a,k,n=int(a), int(k), int(n)
# 
cnt=0
box=(int(a/k)+1)*k
for i in range(box, n+1, k):
    print(i-a, end=' ')
    cnt+=1
# 
if(cnt==0):
    print(-1)