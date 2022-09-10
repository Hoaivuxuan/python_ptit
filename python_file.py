file = input()
check = True
for i in file:
    if (i<'a' and i>'z') or (i<'A' and i>'Z'): check=False
    if i!='.' or i!='_': check=False
    if (file[-2] + file[-1])!='py' : check=False
if check==True : print("yes")
else : print("no")