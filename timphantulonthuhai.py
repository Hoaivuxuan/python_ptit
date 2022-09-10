from os import remove
n = int(input())
arr = map(int, input().split())
arr=set(arr)
arr=list(arr)
arr.sort()
print(arr[-2])