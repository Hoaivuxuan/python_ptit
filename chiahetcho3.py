import numbers


t=int(input())
for i in range(t):
    number=input()
    if int(number)%3==0:
        print("YES")
    else: print("NO")