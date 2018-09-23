n = int(input())
a1 = list(int(i) for i in input().split())
a2 = list(int(i) for i in input().split())

m = 0
for i in range(1,n+1):
    c = 0
    for k in range(0,i):
        c += a1[k]
    for l in range(i-1,n):
        c  += a2[l]
    if c > m:
        m = c
print(m)