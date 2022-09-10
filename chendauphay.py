str=input()[::-1]
res=''
for i in range(0, len(str)):
    res=str[i]+res
    if(i%3==2):
        res=','+res
print(res)