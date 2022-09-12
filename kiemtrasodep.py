t=int(input())
for i in range(t):
    n=input()
    # myset=set()
    check=1
    for i in range(1,len(n)-1):
        if abs(int(n[i]) - int(n[i-1])) != abs(int(n[i]) - int(n[i+1])):
            check=0
    for i in range(0,len(n),2):
        if n[i]!=n[0]: check=0
    if (n[0]!=n[1] and check==1):
        print("YES")
    else : print("NO")