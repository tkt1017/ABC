h,w = map(int,input().split())
ss = []
ssc = []
for i in range(h):
    ss.append(list(input()))
    ssc.append([0]*w)

def hfunc1(i,j):
    if ss[i][j] != "#":
        ssc[i][j] += 1

def hfunc2(i,j):
    xs = -1
    xe = 2
    ys = -1
    ye = 2

    if i == 0:
        xs = 0
    if i == h-1:
        xe = 1
    if j == 0:
        ys = 0
    if j == w-1:
        ye = 1 

    for x in range(xs,xe):
        for y in range(ys,ye):
                hfunc1(i+x,j+y)
    
for i in range(h):
    for j in range(w):
        if ss[i][j] == "#":
            ssc[i][j] = "#"
            hfunc2(i,j)

ans = ""
for x in ssc:
    for y in x:
        ans += str(y)
    ans += "\n"
print(ans)