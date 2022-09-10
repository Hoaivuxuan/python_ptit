def ucln(a,b):
    while(a>0):
        if(a<b):
            a,b=b,a
        a=a%b
    return b
# 
for i in range(int(input())):
    num=input()
    num1=int(num)
    num2=int(num[::-1])
    if ucln(num1, num2)==1:
        print("YES");
    else: print("NO")