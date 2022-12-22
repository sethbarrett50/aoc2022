# Day 9 AoC 2022
# Part 1
import numpy

def main():
    with open('input.txt') as f:
        lines = f.readlines()
    
    head, tail, visited = (0,0), (0,0), set()
    visited.add(tail)

    for line in lines: 
        direct, num = line[0], int(line[2])
        for _ in range(num):
            #tailMove = False if head[0] == tail[0] and head[1] == tail[1] else True

            if direct == 'D': head = (head[0], head[1] - 1)
            elif direct == 'U': head = (head[0], head[1] + 1)
            elif direct == 'L': head = (head[0] - 1, head[1])
            elif direct == 'R': head = (head[0] + 1, head[1])
            # print(head[0])

            subx, suby = head[0] - tail[0], head[1] - tail[1]
            if abs(suby) > 1 or abs(subx) > 1:
                tailx = 1 if subx > 0 else 0 if subx == 0 else -1
                taily = 1 if suby > 0 else 0 if suby == 0 else -1
                tail = (tail[0] + tailx, tail[1] + taily)
                visited.add(tail)

            
    print(len(visited))
                


if __name__ == '__main__':
    main()