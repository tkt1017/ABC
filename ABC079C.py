x = list(input())
n = [int(i) for i in x]

def func(m):
    x1 = m[0] + m[1] + m[2] + m[3]
    if x1 == 7:
        return ("{}+{}+{}+{}=7".format(m[0],m[1],m[2],m[3]))
    x2 = m[0] + m[1] + m[2] - m[3]
    if x2 == 7:
        return ("{}+{}+{}-{}=7".format(m[0],m[1],m[2],m[3]))
    x3 = m[0] + m[1] - m[2] - m[3]
    if x3 == 7:
        return ("{}+{}-{}-{}=7".format(m[0],m[1],m[2],m[3]))
    x4 = m[0] + m[1] - m[2] + m[3]
    if x4 == 7:
        return ("{}+{}-{}+{}=7".format(m[0],m[1],m[2],m[3]))
    x5 = m[0] - m[1] - m[2] + m[3]
    if x5 == 7:
        return ("{}-{}-{}+{}=7".format(m[0],m[1],m[2],m[3]))
    x6 = m[0] - m[1] - m[2] - m[3]
    if x6 == 7:
        return ("{}-{}-{}-{}=7".format(m[0],m[1],m[2],m[3]))
    x7 = m[0] - m[1] + m[2] - m[3]
    if x7 == 7:
        return ("{}-{}+{}-{}=7".format(m[0],m[1],m[2],m[3]))
    x8 = m[0] - m[1] + m[2] + m[3]
    if x8 == 7:
        return ("{}-{}+{}+{}=7".format(m[0],m[1],m[2],m[3]))

print(func(n))