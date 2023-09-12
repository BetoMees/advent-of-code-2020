file = open("day5.txt").read().strip().split("\n")
plane = []
for x in range(128):
    plane.append([])
    for y in range(8):
        plane[x].append(0)

for val in file:
    row_min = 0
    row_max = 127
    col_min = 0
    col_max = 7
    for t in val:
        if t == "F":
            row_max -= int((row_max-row_min)/2)+1
        if t == "B":
            row_min += int((row_max-row_min)/2)+1
        if t == "L":
            col_max -= int((col_max-col_min)/2)+1
        if t == "R":
            col_min += int((col_max-col_min)/2)+1
    if row_min == row_max and col_min == col_max:
        if row_max == 77:
            print(val, col_max)
        plane[row_max][col_max]=1
        # result = row_max * 8 + col_max
        # if result > highest:
        #     highest = result
    else:
        print(val, row_min, row_max, "can enter here")

find=0
for row in range(128):
    for col in range(8):
        if plane[row][col] == 0 and find == 1:
            print(row, col)
            exit(1)
        else:
            find = plane[row][col]


# 617 result