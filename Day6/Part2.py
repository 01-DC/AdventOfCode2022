# full_input = open("test.txt").read().strip().split("\n")[0]
full_input = open("input.txt").read().strip().split("\n")[0]

l, r = 0, 0
chars = []

while r <= 13:
    chars.append(full_input[r])
    r+= 1

while len(set(chars)) != 14:
    chars.remove(full_input[l])
    l+= 1
    chars.append(full_input[r])
    r+= 1
    # print(chars)

print(r)