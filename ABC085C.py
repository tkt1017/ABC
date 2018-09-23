n,y = map(int,input().split())
a = [-1,-1,-1]
flag = False
 
y = y/1000
for k in range(n+1)[::-1]:
    for l in range(n-k+1)[::-1]:
        m = n-(k+l)
        osum = 10*k + 5*l + m
        if osum == y:
            a[0] = k
            a[1] = l
            a[2] = m
            flag = not flag
            break
    if flag:
        break
 
print(a[0], a[1], a[2])