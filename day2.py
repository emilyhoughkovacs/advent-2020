import sys
import os
import re

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'inputday2.txt'
        f = open(file, 'r')
        lines = f.read().splitlines()
        f.close()

        lines = [re.split(r"-| |: ", line) for line in lines]

        lines = [[int(line[0]), int(line[1]), line[2], line[3]] for line in lines]
        lines = [line+[line[3].count(line[2])] for line in lines]

        numValid = 0
        for line in lines:
            if line[4] >= line[0] and line[4] <= line[1]:
                numValid+= 1

        return numValid

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()