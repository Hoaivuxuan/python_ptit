def check(n):
    ok = True
    for c in n:
        if int(c) % 2 != 0:
            ok = False
            break
    return ok

t = int(input())
while t > 0:
    n = int(input())
    a = []
    for i in range(22,n,2):
        s = str(i)
        if(s == s[::-1] and len(s) % 2 == 0 and check(s) == True):
            print(s, end = ' ')
    print("")
    t -= 1