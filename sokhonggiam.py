
T = int(input())
for t in range(0, T):
    a = input()
    check = False
    for i in range(1, len(a)):
        if int(a[i-1]) > int(a[i]):
            print('NO')
            check = True
            break
    if check == False:
        print('YES')
