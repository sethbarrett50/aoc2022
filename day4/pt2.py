# Day 4 AoC 2022
# Part 2
import re

# We love Python sets


def main():
    pattern, sets, num = re.compile(r"([\d]*)-([\d]*),([\d]*)-([\d]*)"), [], 0

    with open('input.txt') as f:
        lines = f.readlines()

    for line in lines:
        match = pattern.match(line)
        start1, end1, start2, end2 = int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))
        sets.append((set(range(start1, end1 + 1)), set(range(start2, end2 + 1))))
    
    for one, two in sets:
        if one&two:
            num += 1
    print(num)


if __name__ == '__main__':
    main()