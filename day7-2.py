file = open("day7.txt").read().strip().replace(
    " bags", "").replace(" bag", "").replace(".", "")

def hasNumber(bp) -> bool:
    if bp[0] in "0123456789":
        return True
    return False

file = file.split("\n")
def findBag(find) -> int:
    if find == "no other":
        return -1
    for f in file:
        f = f.split("contain")
        if find in f[0].strip():
            result = 0
            for bag in f[1].split(","):
                bag = bag.strip()
                if(hasNumber(bag)):
                    num = int(bag[0])
                    bag = bag[2:]
                    result += findBag(bag) * num + num
                else:
                    num = 1
                    result += findBag(bag) * num + num
            return result
    return 0


print(findBag("shiny gold"))

