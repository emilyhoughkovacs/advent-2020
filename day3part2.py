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

        def go_skiing(x=3, y=1):
            currentPosition = 0
            traveled = []
            for line in lines[y:len(lines):y]:
                pool = cycle(line)
                currentPosition+=x
                for i in range(currentPosition):
                    next(pool)
                traveled.append(next(pool))

            return traveled.count("#")

        # print(go_skiing(1))
        # print(go_skiing(3))
        # print(go_skiing(5))
        # print(go_skiing(7))
        # print(go_skiing(1, 2))
        return go_skiing(1)*go_skiing(3)*go_skiing(5)*go_skiing(7)*go_skiing(1, 2)

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()