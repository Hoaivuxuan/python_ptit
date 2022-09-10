N = int(input())
box=[]
for _ in range(N):
    name = list(input().split())
    if name[0]=='insert': box.insert(int(name[1]), int(name[2]))
    elif name[0]=='append': box.append(int(name[1]))
    elif name[0]=='remove': box.remove(int(name[1]))
    elif name[0]=='sort': box.sort()
    elif name[0]=='pop': box.pop()
    elif name[0]=='reverse': box.reverse()
    elif name[0]=='print': print(box)