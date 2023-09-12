file = open("day6.txt").read().strip().split("\n\n")

def hasIn(list, a):
    for q in list:
        if q == a:
            return True
    return False

count = 0
for group in file:
    answers = group.split("\n")
    first = answers[0]
    for a in answers:
        for q in first:
            if not hasIn(a,q):
                first = first.replace(q,"")
        if len(first)==0:
            break
    count += len(first)

print(count)
