# full_input = open("test.txt").read().split("\n")
full_input = open("input.txt").read().split("\n")

S = []
for line in full_input:
    if line == '':
        break
    sz = (len(line)+1)//4
    while len(S) < sz:
        S.append([])
    for i in range(len(S)):
        ch = line[1+4*i]
        if ch != ' ' and 'A'<=ch<='Z':
            S[i].append(ch)

for x in S:
    x.reverse()

found = False
for line in full_input:
    if line=='':
        found = True
        continue
    if not found:
        continue
    cmd = line.split()
    to_move = []
    for i in range(int(cmd[1])):
        n = S[int(cmd[3])-1][-1]
        S[int(cmd[3])-1].pop()
        to_move.append(n)
    to_move.reverse()
    S[int(cmd[5])-1].extend(to_move)
    # print(S)

top = [x[-1] for x in S]
print(''.join(top))