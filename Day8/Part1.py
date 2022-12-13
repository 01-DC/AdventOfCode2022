# grid = open("test.txt").read().strip().split("\n")
grid = open("input.txt").read().strip().split("\n")

rows, cols= len(grid), len(grid[0])

total_score = 2*(rows + cols) - 4
# print(total_score)

def checkDirs(i, j) -> bool:
    flag = [1, 1, 1, 1]
    for x in range(0, j):
        if int(grid[i][x]) >= int(grid[i][j]):
            flag[0]= 0

    for x in range(cols-1, j, -1):
        if int(grid[i][x]) >= int(grid[i][j]):
            flag[1]= 0
        
    for y in range(0, i):
        if int(grid[y][j]) >= int(grid[i][j]):
            flag[2]= 0

    for y in range(rows-1, i, -1):
        if int(grid[y][j]) >= int(grid[i][j]):
            flag[3]= 0
    return sum(flag)>0
        
for i in range(1, rows-1):
    for j in range(1, cols-1):
        if checkDirs(i, j):
            total_score+= 1

print(total_score)
