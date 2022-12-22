# Day 10 AoC 2022
# Part 1
import re

def check(cycle, x):
    correct = [20, 60, 100, 140, 180, 220]
    if cycle in correct:
       return x * cycle
    else:
        return 0 


def main():
    with open('input.txt') as f:
        lines = f.readlines()

    patt = re.compile(r"\w* (-\d*|\d*)")
    x, cycle, sumNum = 1, 0, 0
    for line in lines:
        if line[0] == 'n':
            cycle += 1
            sumNum += check(cycle, x)
        else: 
            num = int(patt.match(line).group(1))
            # if num < 0: print(num,end='')
            for _ in range(2):
                cycle += 1
                sumNum += check(cycle, x)
            x += num
    print(sumNum)

if __name__ == '__main__':
    main()



    