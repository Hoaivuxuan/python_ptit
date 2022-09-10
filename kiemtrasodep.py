t=int(input())
for i in range(t):
    n=input()
    myset=set()
    check=1
    for i in range(0, len(n)-2):
        myset.add(n[i])
        if n[i]!=n[i+2]: 
            check=0
    if (len(myset)==2 and check==1):
        print("YES")
    else : print("NO")