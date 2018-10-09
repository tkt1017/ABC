n = int(input())
t = [int(input()) for i in range(n)]
def bfunc(n):
    blist = []
    for i in range(2**(n)):
        blist.append(list(map(int,list(bin(i)[2::].zfill(n)))))
    return blist
blist = bfunc(n)

x = 200
for nums in blist:
    x0 = 0
    x1 = 0
    for k,num in enumerate(nums):
        if num == 0:
            x0 += t[k]
        elif num == 1:
            x1 += t[k]
    cx = max(x0,x1)
    x = min(x,cx)
print(x)