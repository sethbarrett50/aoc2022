# Day 3 AoC 2022
# Part 1




def main():
    letters = [c for c in list(map(chr,range(ord('a'),ord('z')+1)))]
    letters.extend([c for c in list(map(chr,range(ord('A'),ord('Z')+1)))])
    priorities, sumPrioriites = dict(zip(letters, [int(x) for x in range(1, 52+1)])),  0

    with open('input.txt') as f:
        lines = f.readlines()

    for line in lines:
        sumPrioriites += priorities[str(list(set(line[:len(line)//2])&set(line[len(line)//2:])))[2:-2]]
    print(sumPrioriites)

        



if __name__ == '__main__':
    main()