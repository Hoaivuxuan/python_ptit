from inspect import stack
# 
box=[]
N=int(input())
arr=[int(i) for i in input().split()]
for i in arr:
    if len(box)==0 or (i+box[-1])%2!=0 :
        box.append(i)
    else: box.pop()
print(len(box))
