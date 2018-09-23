n = int(input())
a = list(map(int, input().split()))
flag = True
count = 0

while flag:
    for i in range(n):
        if a[i]%2 == 0:
            a[i] = a[i]/2
        else:
            print(count)
            flag = not flag
            break
    count += 1


