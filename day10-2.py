numbers = list(map(int, open("day10.txt").read().strip().split("\n")))

# numbers.sort()


# def dig(num, j1, j3):
#     if len(num) == 1:
#         return j1+1, j3+1
#     res = num[1] - num[0]
#     if(res == 1):
#         j1 += 1
#     elif res == 3:
#         j3 += 1
#     return dig(num[1:], j1, j3)


# j1, j3 = dig(numbers, 0, 0)
# print(j1 * j3)
