# https://adventofcode.com/2020/day/4#part2
file = open("day4.txt").read().strip().split("\n\n")
eyeList = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def checkRange(val, range):
    _min, _max = range.split("-")
    if not (val >= _min and val <= _max):
        return False
    return True


def checkRangeList(val, range):
    _min1, _max1 = range[0].split("-")
    _min2, _max2 = range[1].split("-")
    for v in val:
        if not (v >= _min1 and v <= _max1 or v >= _min2 and v <= _max2):
            print(v >= _min1 and v <= _max1, v >= _min2 and v <= _max2)
            print(v, val, range,)
            return False
    return True


def hairColor(val):
    if len(val) != 7 or "#" != val[0]:
        return False
    return checkRangeList(val[1:], ["0-9", "a-f"])


def checkHgt(value):
    if "cm" in value:
        return checkRange(value.replace("cm", ""), "150-193")
    elif "in" in value:
        return checkRange(value.replace("in", ""), "59-76")
    return False


def isValid(cod, value):
    if cod == "byr":
        return checkRange(value, "1920-2002")
    elif cod == "iyr":
        return checkRange(value, "2010-2020")
    elif cod == "eyr":
        return checkRange(value, "2020-2030")
    elif cod == "hcl":
        return hairColor(value)
    elif cod == "pid":
        return value.isnumeric() and len(value) == 9
    elif cod == "hgt":
        return checkHgt(value)
    elif cod == "ecl":
        return value in eyeList
    elif cod == "cid":
        return False
    print(cod, "cound come here")
    return False


def validData(val):
    c = 0
    for v in val:
        cod, v = v.split(":")
        if isValid(cod, v):
            c += 1
    return c


def hasCid(val):
    for v in val:
        cod, _ = v.split(":")
        if cod == "cid":
            return True
    return False


def testa(file):
    r = file.replace("\n", " ").split(" ")
    if((len(r) == 8 or len(r) == 7 and not hasCid(r)) and validData(r) == 7):
        return 1
    return 0


c = 0
for f in file:
    c += testa(f)
print(c)
