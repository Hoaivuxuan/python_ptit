t=int(input())
for i in range(t):
    str=input()
    for i in range(1, len(str),2):
        for j in range(0,int(str[i])):
            print(str[i-1], end='')
    # 
    print('')