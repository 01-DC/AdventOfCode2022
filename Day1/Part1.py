# full_input = open("test.txt").read().strip().split("\n")
full_input = open("input.txt").read().strip().split("\n")

max_calories= 0
current_calories= 0
for line in full_input:
    if line != "":
        current_calories += int(line)
    else:
        max_calories= max(max_calories, current_calories)
        current_calories= 0
max_calories= max(max_calories, current_calories)

print(max_calories)