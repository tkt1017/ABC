n = int(input())
a = [None]
for j in range(n):
    a.append(int(input()))

i = 1
c = 0
r = [1]
while True:
    c += 1
    i = a[i]
    if i == 2:
        print(c)
        break
    if c > (10**5):
        print(-1)
        break
