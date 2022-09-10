str=input()
low=0
up=0
for i in str:
    if(i>='A' and i<='Z'): up+=1
    elif(i>='a' and i<='z'): low+=1
# 
if(low>=up): print(str.lower())
elif(up>low): print(str.upper())