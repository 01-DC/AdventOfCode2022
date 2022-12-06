# full_input = open("test.txt").read().strip().split("\n")
full_input = open("input.txt").read().strip().split("\n")

winner = {'A' : 2, 'B' : 3, 'C' : 1}
draw = {'A' : 1, 'B' : 2, 'C' : 3}
lose = {'A' : 3, 'B' : 1, 'C' : 2}

total_score= 0
for line in full_input:
    if line[2] == 'Z':
        total_score+= winner[line[0]] + 6
    elif line[2] == 'Y':
        total_score+= draw[line[0]] + 3
    else:
        total_score+= lose[line[0]]

print(total_score)