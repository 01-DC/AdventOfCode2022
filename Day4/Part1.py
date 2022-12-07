# full_input = open("test.txt").read().strip().split("\n")
full_input = open("input.txt").read().strip().split("\n")

range_count =  0
for line in full_input:
    lrange, rrange = line.split(',')
    lrange = list(map(int, lrange.split('-')))
    rrange = list(map(int, rrange.split('-')))
    if (lrange[0]<=rrange[0] and lrange[1]>=rrange[1]) or (lrange[0]>=rrange[0] and lrange[1]<=rrange[1]):
        range_count+= 1

print(range_count)