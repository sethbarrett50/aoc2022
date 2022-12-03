# Day 1 AoC 2022
# Part 2




def main():
    lines, moves, score = [], [], 0
    with open('input.txt') as f:
        lines = f.readlines() 
    
    moveScore = {
        'AY': 2 + 6,
        'AX': 1 + 3,
        'AZ': 3 + 0,
        'BY': 2 + 3,
        'BX': 1 + 0,
        'BZ': 3 + 6,
        'CY': 2 + 0,
        'CX': 1 + 6,
        'CZ': 3 + 3
    }

    for line in lines:
        moves = line.replace("\n", "").split()
        score += moveScore[f'{moves[0]}{moves[1]}']
    print(score)



if __name__ == '__main__':
    main()