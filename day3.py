file = open("input.txt").read().strip().split("\n")

def get(down, right):
    c=0
    if down >= len(file):
        return 0
    if right >= len(file[down]):
        right-=len(file[down])
    if file[down][right] == "#":
        c+=1
    c+=get(down+1,right+3)
    return c



print(get(1,3))