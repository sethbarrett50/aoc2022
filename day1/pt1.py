# Day 1 AoC 2022
# Part 2




def main():
    maxWeight, lines, currentElfWeight = 0, [], 0

    with open('input.txt') as f:
        lines = f.readlines() 
    
    for line in lines:
        if line == '\n':
            if currentElfWeight > maxWeight:
                maxWeight = currentElfWeight
            currentElfWeight = 0
        else:
            currentElfWeight += int(line)
    print(f'Max Weight Carried by an elf: {maxWeight}')



if __name__ == '__main__':
    main()