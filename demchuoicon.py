def count_string(a, b):
    cnt = 0
    for i in range(0, len(a)):
        cnt += a.count(b,i,i+len(b))
    return cnt
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)