sr = input()
n = len(sr)

blist = []
for i in range(2**(n-1)):
    blist.append(list(map(int,list(bin(i)[2::].zfill(n-1)))))

ssum = 0
for k,num in enumerate(blist):
    bi = 0
    bsum = 0
    for i,j in enumerate(num):
        if j == 1:
            bsum += int(sr[bi:i+1])
            bi = i+1
        if i == (len(num)-1):
            bsum += int(sr[bi:])
    ssum += bsum
print(ssum)