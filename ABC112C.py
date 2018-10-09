n = int(input())
l = []
for i in range(n):
    ex,ey,eh = map(int,input().split())
    if eh != 0:
        l.append([ex,ey,eh])

def func2(cx,cy,l):
    ans = l[2] + abs(l[0]-cx) +  abs(l[1]-cy)
    return ans

if len(l) == 1:
    print(l[0][0], l[0][1], l[0][2])
    exit()

for i in range(101):
    for j in range(101):
        for k in range(len(l)-1):
            if func2(i,j,l[k]) == func2(i,j,l[k+1]):
                if k == len(l)-2:
                    print(i, j, func2(i,j,l[k]))
                    exit()
            else:
                break