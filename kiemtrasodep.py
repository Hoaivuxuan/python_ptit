t=int(input())
for i in range(t):
    n=input()
    myset=set()
    check=1
    for i in range(0, len(n)-2):
        myset.add(n[i])
    for i in range(0,len(n),2):
        if n[i]!=n[0]: check=0
    if (n[0]!=n[1] and len(myset)==2 and check==1):
        print("YES")
    else : print("NO")