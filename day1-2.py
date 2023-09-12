n = open("day1.txt").read().strip().split("\n")


def testa(val1, val2, prox):
    for r2 in prox:
        if int(val1)+int(val2)+int(r2) == 2020:
            print(val1,val2,r2)
            print(int(val1)*int(val2)*int(r2))
            return True
    return False

tam = len(n)
end = False;
for r1 in range(tam):
    for r2 in range(tam - r1):
        end = testa(n[r1], n[r2], n[r2:])
        if(end):
            break
    if(end):
        break