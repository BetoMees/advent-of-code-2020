file = open("day7.txt").read().strip().replace(
    " bags", "").replace(" bag", "").replace(".", "")


class bag:
    def __init__(self, name, father):
        self.name = name
        if(father == None):
            self.fatherPos = []
        else:
            self.fatherPos = [father]

    def __str__(self) -> str:
        return self.name

    def getName(self) -> str:
        return self.name

    def getFather(self) -> list:
        return self.fatherPos

    def addFather(self, father):
        if not father in self.fatherPos:
            self.fatherPos.append(father)



class listBags:
    def __init__(self):
        self.bags = []

    def insert(self, father, bp):
        bpPos = self.findBag(bp)
        if(bpPos != -1):
            fatherPos = self.findBag(father)
            if(fatherPos != -1):
                self.bags[bpPos].addFather(fatherPos)
            else:
                self.bags.append(bag(father, None))
                self.bags[bpPos].addFather(len(self.bags)-1)
        else:
            fatherPos = self.findBag(father)
            if(fatherPos != -1):
                self.bags.append(bag(bp, fatherPos))
            else:
                self.bags.append(bag(father, None))
                self.bags.append(bag(bp, len(self.bags)-1))
                pass

    def findBag(self, bag) -> int:
        for i in range(len(self.bags)):
            if(bag == self.bags[i].getName()):
                return i
        return -1

    def getBags(self):
        return self.bags


lista = listBags()

num = "0123456789"
for n in num:
    file = file.replace(n, "")
file = file.split("\n")

for f in file:
    f = f.split("contain")
    child = f[1].split(",")
    for c in child:
        lista.insert(f[0].strip(), c.strip())

def digBag(list,pos):
    c = pos
    for p in pos:
        c+=digBag(list, list[p].getFather())
    return c

goldPos = lista.findBag("shiny gold")
bags = lista.getBags()
clist= digBag(bags,bags[goldPos].getFather())
clean = []
for c in clist:
    if not c in clean:
        clean.append(c)

print(len(clean))