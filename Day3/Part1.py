# full_input = open("test.txt").read().strip().split("\n")
full_input = open("input.txt").read().strip().split("\n")

total_score= 0
for line in full_input:
    left, right = set(line[:len(line)//2]), set(line[len(line)//2:])
    diff= left.intersection(right)
    c= diff.pop()
    if c.islower():
        total_score+= ord(c)-96
    else:
        total_score+= ord(c)-38

print(total_score)