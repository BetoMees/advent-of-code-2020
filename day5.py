file = open("day5.txt").read().strip().split("\n")

highest = 0
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
        result = row_max * 8 + col_max
        if result > highest:
            highest = result
    else:
        print(val, row_min, row_max, "can't enter here")

print(highest)