from collections import Counter

n = int(input())
v = list(map(int,input().split()))
v0 = []
v1 = []
for i,ev in enumerate(v):
    if i%2 == 0:
        v0.append(ev)
    else:
        v1.append(ev)

mcv0 = Counter(v0).most_common(2)
mcv1 = Counter(v1).most_common(2)
cmcv0 = mcv0[0][1]
cmcv1 = mcv1[0][1]
ans = n - cmcv0 - cmcv1
if mcv0[0][0] == mcv1[0][0]:
    if (len(mcv0) == 1) and (len(mcv1) == 1):
        ans = int(n/2)
    else:
        ans = min(n - mcv0[1][1] - cmcv1, n - cmcv1 - mcv1[1][1])
print(ans)

