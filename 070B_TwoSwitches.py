n = list(map(int, input().split()))

def func1(k,l):
    if k>l:
        return l
    else:
        return k

def func(x):
    if (x[2]>x[1]) or (x[0]>x[3]):
        return 0
    else:
        if x[0]>x[2]:
            return (func1(x[1],x[3])-x[0])
        else:
            return (func1(x[1],x[3])-x[2])

print(func(n))
