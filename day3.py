import sys
import os
from itertools import cycle

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'inputday3.txt'
        f = open(file, 'r')
        lines = f.read().splitlines()
        f.close()

        currentPosition = 0
        traveled = []
        for line in lines[1:]:
            pool = cycle(line)
            currentPosition+=3
            for i in range(currentPosition):
                next(pool)
            traveled.append(next(pool))

        return traveled.count("#")

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()