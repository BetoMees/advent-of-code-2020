file = open("day2.txt").read().strip().split("\n")

def checkVal(letter, value):
    c = 0
    for v in value:
        if letter == v:
            c+=1
    return c

def testa(val):
    rule, val = val.split(": ")
    minmax, l = rule.split(" ")
    r = checkVal(l,val)
    _min, _max = minmax.split("-")
    if(int(_min)<= r & r <= int(_max)):
        return 1
    return 0


c=0
for f in file:
    c+=testa(f)
print(c)