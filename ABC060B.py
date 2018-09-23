a,b,c = map(int,input().split())
res = []
i = 1
while True:
    r = (a * i) % b
    if r == c:
        print("YES")
        break
    else:
        if r in res:
            print("NO")
            break
        else:
            res.append(r)
    i += 1