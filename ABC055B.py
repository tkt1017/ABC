n = int(input())
x = 1
Y = 10**9+7
for z in range(1,n+1):
    x = x*z
    if x >= Y:
        x = x % Y
print(x)