# full_input = open("test.txt").read().strip().split("\n")
full_input = open("input.txt").read().strip().split("\n")

all_calories= []
current_calories= 0
for line in full_input:
    if line != "":
        current_calories += int(line)
    else:
        all_calories.append(current_calories)
        current_calories= 0
all_calories.append(current_calories)

all_calories.sort(reverse=True)
# print(all_calories)
print(sum(all_calories[0:3]))
