# full_input = open("test.txt").read().strip().split("\n")
full_input = open("input.txt").read().strip().split("\n")

total_score= 0
for i in range(0, len(full_input), 3):
    e1, e2, e3 = set(full_input[i]), set(full_input[i+1]), set(full_input[i+2])
    diff= e1.intersection(e2, e3)
    c= diff.pop()
    if c.islower():
        total_score+= ord(c)-96
    else:
        total_score+= ord(c)-38

print(total_score)