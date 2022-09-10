def ucln(a,b):
    while(a>0):
        if(a<b):
            a,b=b,a
        a%=b
    return b
# 
l,r=map(int, input().split())
box=[]
for i in range(l, r-1):
    for j in range(i+1, r):
        if ucln(i,j)==1:
            box.append([i,j])
# 
for k in box:
    for i in range(k[1]+1, r+1):
        if (ucln(i, k[0])==1) and (ucln(i, k[1])==1):
            print('(' + str(k[0]) + ', ' + str(k[1]) + ', ' + str(i) + ')')