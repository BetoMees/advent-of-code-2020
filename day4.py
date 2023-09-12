file = open("day4.txt").read().strip().split("\n\n")

def hasCid(val):
    for v in val:
        cod, _ = v.split(":")
        if cod == "cid":
            return True
    return False
def testa(file):
    r = file.replace("\n", " ").split(" ")
    if(len(r)==8 or len(r) == 7 and not hasCid(r)):
        return 1
    return 0

c=0
for f in file:
    c+=testa(f)
print(c)