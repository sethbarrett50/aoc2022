# Day 9 AoC 2022
# Part 2 
import numpy as np

def main():
    with open('input.txt') as f:
        lines = f.readlines()
    visited, knots = set(),[(0,0,)]* 10
    # knots[5] = (0,3)
    visited.add(knots[-1])
    for line in lines:
        direct, num = line[0], int(line[2])
        for _ in range(num):
            if direct == 'D': knots[0] = (knots[0][0], knots[0][1] - 1)
            elif direct == 'U': knots[0] = (knots[0][0], knots[0][1] + 1)
            elif direct == 'L': knots[0] = (knots[0][0] - 1, knots[0][1])
            elif direct == 'R': knots[0] = (knots[0][0] + 1, knots[0][1])
            for i in range(9):
                diff_x = knots[i][0] - knots[i+1][0]
                diff_y = knots[i][1] - knots[i+1][1]
                if abs(diff_x) > 1 or abs(diff_y) > 1:
                    knots[i+1] = (knots[i+1][0] + np.sign(diff_x), knots[i+1][1] + np.sign(diff_y))
                visited.add(knots[-1])
    print(len(visited))

    

if __name__ == '__main__':
    main()

