t=int(input())
for i in range(t):
    N=input()
    first=N[0]+N[1]
    last=N[-2]+N[-1]
    if(int(first)==int(last)): print("YES")
    else: print("NO")