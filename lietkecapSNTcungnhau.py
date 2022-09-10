def gcd(a, b):
    while (a > 0):
        if a < b:
            a, b = b, a
        a %= b
    return b
# 
t=int(input())
for i in range(t):
    arr = map(int, input().split())
    box = sorted(arr)
    for i in range(0, len(box)-1):
        for j in range(i+1, len(box)):
            if gcd(box[i],box[j]) == 1:
                print(box[i] , box[j])
                # print("")