# Day 1 AoC 2022
# Part 2




def main():
    lines, currentElfWeight = [], 0
    elfWeights = []

    with open('input.txt') as f:
        lines = f.readlines() 
    
    for line in lines:
        if line != '\n':
            currentElfWeight += int(line)

        else:
            elfWeights.append(currentElfWeight)
            currentElfWeight = 0

    elfWeights.sort()
    print(elfWeights)
    sumElfWeights = sum(elfWeights[-3:])
    print(f'Max Weight Carried by the top three elves: {sumElfWeights}')



if __name__ == '__main__':
    main()