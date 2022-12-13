import math

# grid = open("test.txt").read().strip().split("\n")
grid = open("input.txt").read().strip().split("\n")

rows, cols= len(grid), len(grid[0])

max_score = 0
# print(total_score)

def prodOfDirs(i, j):
    rng = [0, 0, 0, 0]
    for x in range(j+1, cols):
        if int(grid[i][x]) < int(grid[i][j]):
            rng[0]+= 1
        else:
            rng[0]+= 1
            break
        
    for x in range(j-1, -1, -1):
        if int(grid[i][x]) < int(grid[i][j]):
            rng[1]+= 1
        else:
            rng[1]+= 1
            break
        
    for y in range(i+1, rows):
        if int(grid[y][j]) < int(grid[i][j]):
            rng[2]+= 1
        else:
            rng[2]+= 1
            break

    for y in range(i-1, -1, -1):
        if int(grid[y][j]) < int(grid[i][j]):
            rng[3]+= 1
        else:
            rng[3]+= 1
            break

    # print(rng)
    return math.prod(rng)
        
for i in range(1, rows-1):
    for j in range(1, cols-1):
        max_score = max(max_score, prodOfDirs(i, j))

print(max_score)
