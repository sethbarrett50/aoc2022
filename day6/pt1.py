# Day 6 AoC 2022
# Part 1
import re
# print("Pt1#: {pt1}\nPt2#: {pt2}\n".format(pt1=re.search(r'(\w)(?!\1)(\w)(?!\1|\2)(\w)(?!\1|\2|\3)(\w)', open('input.txt').read()).start() + 4, pt2=re.search(r'(\w)(?!\1)(\w)(?!\1|\2)(\w)(?!\1|\2|\3)(\w)(?!\1|\2|\3|\4)(\w)(?!\1|\2|\3|\4|\5)(\w)(?!\1|\2|\3|\4|\5|\6)(\w)(?!\1|\2|\3|\4|\5|\6|\7)(\w)(?!\1|\2|\3|\4|\5|\6|\7|\8)(\w)(?!\1|\2|\3|\4|\5|\6|\7|\8|\9)(\w)(?!\1|\2|\3|\4|\5|\6|\7|\8|\9|\10)(\w)(?!\1|\2|\3|\4|\5|\6|\7|\8|\9|\10|\11)(\w)(?!\1|\2|\3|\4|\5|\6|\7|\8|\9|\10|\11|\12)(\w)(?!\1|\2|\3|\4|\5|\6|\7|\8|\9|\10|\11|\12|\13)\w', open('input.txt').read()).start() + 14)) lol

def main():
    pattern = re.compile(r'(\w)(?!\1)(\w)(?!\1|\2)(\w)(?!\1|\2|\3)(\w)')
    with open('input.txt') as f:
        lines = f.readlines()

    match = pattern.search(lines[0])
    print(f'Chr #: {match.start() + 4}')



        



if __name__ == '__main__':
    main()