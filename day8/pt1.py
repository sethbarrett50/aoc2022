# Day 8 AoC 2022
# Part 1

def main():
    grid, cnt =  [], 0
    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines:
        grid.append(list(map(int, list(line[:-1]))))
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            element, isEdge  = grid[i][j], i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1
            if isEdge:
                cnt += 1
                continue
            
            # Left
            for x in range(0, j):
                if element <= grid[i][x]:
                    break
            else:
                cnt += 1
                continue

            # Right
            for x in range(j + 1, len(grid[0])):
                if element <= grid[i][x]:
                    break
            else:
                cnt += 1
                continue

            # Top
            for y in range(0, i):
                if element <= grid[y][j]:
                    break
            else:
                cnt += 1
                continue

            # Bottom
            for y in range(i + 1, len(grid)):
                if element <= grid[y][j]:
                    break
            else:
                cnt += 1
                continue

    print(f'Num visible trees: {cnt}')

        



if __name__ == '__main__':
    main()