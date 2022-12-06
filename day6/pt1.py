# Day 6 AoC 2022
# Part 1
import re

def main():
    pattern = re.compile(r'(\w)(?!\1)(\w)(?!\1|\2)(\w)(?!\1|\2|\3)(\w)')
    with open('input.txt') as f:
        lines = f.readlines()

    match = pattern.search(lines[0])
    print(f'Chr #: {match.start() + 4}')



        



if __name__ == '__main__':
    main()