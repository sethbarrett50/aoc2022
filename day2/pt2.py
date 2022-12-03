# Day 1 AoC 2022
# Part 2




def main():
    lines, moves, score = [], [], 0
    with open('input.txt') as f:
        lines = f.readlines() 
    
    # 1st: A for Rock, B for Paper, and C for Scissors
    # 2nd: X means lose, Y means draw, and Z means win
    # 1 for Rock, 2 for Paper, and 3 for Scissors
    moveScore = {
        'AY': 1 + 3,
        'AX': 3 + 0,
        'AZ': 2 + 6,

        'BY': 2 + 3,
        'BX': 1 + 0,
        'BZ': 3 + 6,

        'CY': 3 + 3,
        'CX': 2 + 0,
        'CZ': 1 + 6
    }

    for line in lines:
        moves = line.replace("\n", "").split()
        score += moveScore[f'{moves[0]}{moves[1]}']
    print(score)



if __name__ == '__main__':
    main()