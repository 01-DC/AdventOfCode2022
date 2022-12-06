# full_input = open("test.txt").read().strip().split("\n")
full_input = open("input.txt").read().strip().split("\n")
scores = {'X' : 1, 'Y' : 2, 'Z' : 3}
winner = {'A' : 'Y', 'B' : 'Z', 'C' : 'X'}
draw = {'A' : 'X', 'B' : 'Y', 'C' : 'Z'}

total_score= 0
for line in full_input:
    total_score+= scores[line[2]]
    if winner[line[0]] == line[2]:
        total_score+= 6
    elif draw[line[0]] == line[2]:
        total_score+= 3

print(total_score)