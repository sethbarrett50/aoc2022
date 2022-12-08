# Day 8 AoC 2022
# Part 2 -> Scenic Treehouse time

def main():
    lines, grid, best = [], [], 0
    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines:
        grid.append(list(map(int, list(line[:-1]))))
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            element, isEdge  = grid[i][j], i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1
            if isEdge: continue # Not good treehouse location
            tmpScore = 1

            # Left
            counter = 0
            for x in reversed(range(0, j)):
                counter += 1
                if element <= grid[i][x]: break
            tmpScore *= counter

            # Right
            counter = 0
            for x in range(j + 1, len(grid[0])):
                counter += 1
                if element <= grid[i][x]: break
            tmpScore *= counter

            # Top
            counter = 0
            for y in reversed(range(0, i)):
                counter += 1
                if element <= grid[y][j]: break
            tmpScore *= counter

            # Bottom
            counter = 0
            for y in range(i + 1, len(grid)):
                counter += 1
                if element <= grid[y][j]: break
            tmpScore *= counter

            if tmpScore > best: best = tmpScore
    print(f'Best Score: {best}')

if __name__ == '__main__':
    main()