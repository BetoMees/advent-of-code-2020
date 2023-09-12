file = open("day3.txt").read().strip().split("\n")

def get2(down, right, rule):
    c=0
    if down >= len(file):
        return 0
    if right >= len(file[down]):
        right-=len(file[down])
    if file[down][right] == "#":
        c+=1
    c+=get2(down+rule[0],right+rule[1], rule)
    return c

def get(list):
    c=1
    for down, right in list:
        r=get2(down, right, [down,right])
        print(r)
        c*=r
    return c

list = [[1,1], [1,3],[1,5],[1,7],[2,1]]
print(get(list))