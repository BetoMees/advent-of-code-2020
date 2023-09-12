file = open("day6.txt").read().strip().split("\n\n")

count = 0
for f in file:
    answered = f.replace("\n", "")
    questions = []
    for a in answered:
        if not a in questions:
            questions.append(a)
            count += 1
print(count)
