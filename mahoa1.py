for i in range(int(input())):
    s=input()
    s=s+' '
    cnt=1
    box=''
    for i in range(1,len(s)):
        if(s[i]==s[i-1]):
            cnt+=1
        else:
            box=box + str(cnt) + s[i-1]
            cnt=1
    print(box)