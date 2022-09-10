a=[]
b=[]
for i in range(int(input())):
    a.append(input())
    b.append(float(input()))
m=min(b) 
box=[]
for i in range(len(b)):
    if b[i]==m : b[i]=100000
m=min(b)
for i in range(len(b)): 
    if b[i]==m : box.append(a[i])
box.sort()
for i in box : print(i)
