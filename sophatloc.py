t = int(input())
for i in range(t):
    N=input()
    size=len(N)
    if(size>=2 and N[-2]=='8' and N[-1]=='6') : print("YES")
    else: print("NO")