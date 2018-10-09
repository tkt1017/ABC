h,w = map(int,input().split())

all_list = []
start = []
cur = []
visit_list = []
visited_list = []
for i in range(h):
    a = list(input())
    all_list.append(a)
    for j in range(w):
        if a[j] == 's':
            start.append(i)
            start.append(j)

def checkgoal(ccur):
    flag = True
    if ccur[0]<=h-2:
        if all_list[ccur[0]+1][ccur[1]] == 'g':
            flag = False
            print("Yes")
            exit()
    if ccur[1]<=w-2:
        if all_list[ccur[0]][ccur[1]+1] == 'g':
            flag = False
            print("Yes")
            exit()
    if ccur[0]>=1:
        if all_list[ccur[0]-1][ccur[1]] == 'g':
            flag = False
            print("Yes")
            exit()
    if ccur[1]>=1:
        if all_list[ccur[0]][ccur[1]-1] == 'g':
            flag = False
            print("Yes")
            exit()
    return flag


def fsearch(ccur):
    if checkgoal(ccur):     
        if ccur[0]<=h-2:
            if (all_list[ccur[0]+1][ccur[1]] != '#')\
            and ([ccur[0]+1,ccur[1]] not in visited_list)\
            and ([ccur[0]+1,ccur[1]] not in visit_list):
                visit_list.append(ccur)
                cur = [ccur[0]+1,ccur[1]]
                fsearch(cur)
        if ccur[1]<=w-2:
            if (all_list[ccur[0]][ccur[1]+1] != '#')\
            and ([ccur[0],ccur[1]+1] not in visited_list)\
            and ([ccur[0],ccur[1]+1] not in visit_list):
                visit_list.append(ccur)
                cur = [ccur[0],ccur[1]+1]
                fsearch(cur)
        if ccur[0]>=1:
            if (all_list[ccur[0]-1][ccur[1]] != '#')\
            and ([ccur[0]-1,ccur[1]] not in visited_list)\
            and ([ccur[0]-1,ccur[1]] not in visit_list):
                visit_list.append(ccur)
                cur = [ccur[0]-1,ccur[1]]
                fsearch(cur)
        if ccur[1]>=1:
            if (all_list[ccur[0]][ccur[1]-1] != '#')\
            and ([ccur[0],ccur[1]-1] not in visited_list)\
            and ([ccur[0],ccur[1]-1] not in  visit_list):
                visit_list.append(ccur)
                cur = [ccur[0],ccur[1]-1]
                fsearch(cur)

        visited_list.append(ccur)
        cur = visit_list.pop()
        if cur == start:
            print("No")
            exit()
        else:
            fsearch(cur)

fsearch(start)
    


        