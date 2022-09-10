P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while(True):
    my_str=input().split()
    k=int(my_str[0])
    if(k==0):
        break
    S=my_str[1]
    box=''
    for i in S:
        can=P.find(i)
        box=box + P[(can+k)%28]
    print(box)