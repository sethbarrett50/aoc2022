# Day 7 AoC 2022
# Part 1
import re

dirRemovePattern = re.compile(r"\w*/$")
cdCommandPattern = re.compile(r"\$ \w* ([\w|\./]*)")
dirCapturePattern = re.compile(r"dir (\w*)")
fileSizeCapturePattern = re.compile(r"(\d*) ")


def genDirSizes(lines:list) -> dict:
    pwd, dirToSize = '', {'/':0}
    for line in lines:
        # If line contains command
        if line[0] == '$':
            # Continue on ls commands
            if line[2] == 'l':
                continue
            commandOperand = cdCommandPattern.match(line).group(1)
            if commandOperand == '..' and pwd != '/':
                pwd = dirRemovePattern.sub("", pwd)
            elif commandOperand != '/':
                pwd = f'{pwd}{commandOperand}/'   

        # If line commands ls output
        else:
            if line[0] == 'd':
                dirToSize[f'{pwd}{dirCapturePattern.match(line).group(1)}/'] = 0
            else:
                fileSize = fileSizeCapturePattern.match(line).group(1)
                tmpDir = pwd
                while tmpDir != '':
                    dirToSize[tmpDir] += int(fileSize)
                    tmpDir = dirRemovePattern.sub("", tmpDir)
    return dirToSize



def main():
    
    with open('input.txt') as f:
        lines = f.readlines()

    dirs = genDirSizes(lines)
    sumSize = 0
    for val in dirs.values():
        if val <= 100000:
            sumSize += val
    print(sumSize)
            



        



if __name__ == '__main__':
    main()