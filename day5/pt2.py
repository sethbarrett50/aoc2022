# Day 5 AoC 2022
# Part 2

import collections, re, pdb

def main():
    stacks, pattern = [], re.compile(r"move ([\d]*) from ([\d]) to ([\d])")
    for _ in range(0,10):
        stacks.append(collections.deque())
    
    with open('input.txt') as f:
        lines = f.readlines()

    # Lines[0:8] are intial stack 
    initStack = ['GTRW', 'GCHPMSVW', 'CLTSGM', 'JHDMWRF', 'PQLHSWFJ', 'PJDNFMS', 'ZBDFGCSJ', 'RTB', 'HNWLC']
    for stack, word in zip(stacks, initStack):
        for c in word:
            stack.append(c)

    # pdb.set_trace()
    for line in lines[10:]:
        match = pattern.match(line)
        numMoved, startStack, endStack = int(match.group(1)), int(match.group(2)) - 1, int(match.group(3)) - 1
        
        movingCrates = collections.deque()
        for _ in range(0, numMoved):
            movingCrates.append(stacks[startStack].pop())

        for _ in range(0, len(movingCrates)):
            stacks[endStack].append(movingCrates.pop())
    
    for stack in stacks:
        if len(stack) != 0:
            print(stack.pop(),end="")
    print()

        



if __name__ == '__main__':
    main()