data = {}
for _ in range(int(input())):
    name, *score = input().split()
    data[name] = [float(m) for m in score]
score = data[input()]
print('%.2f' % (sum(score)/3))