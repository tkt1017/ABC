h,w = map(int,input().split())
ss = []
for i in range(h):
    ss.append(list(input()))

def search(i,j):
    c = 0

    if i != 0:
        if ss[i-1][j] == "#":
            c += 1
    if i != h-1:
        if ss[i+1][j] == "#":
            c += 1
    if j != 0:
        if ss[i][j-1] == "#":
            c += 1
    if j != w-1:
        if ss[i][j+1] == "#":
            c += 1

    if c > 0:
        return False
    else:
        return True

ans = "Yes" 
for i in range(h):
    for j in range(w):
        if ss[i][j] == "#":
            if search(i,j):
                ans = "No"
                break

print(ans)