t=int(input())
for i in range(t):
    num=input()
    sum=0
    inte=1
    for i in range(0, len(num)):
        if i%2==1:
            sum+=int(num[i])
        else:
            if(num[i]!='0'):
                inte*=int(num[i])
    print(inte,sum)