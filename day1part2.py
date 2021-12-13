import sys
import os

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'inputday1.txt'
        f = open(file, 'r')
        lines = f.read().splitlines()
        f.close()

        lines = [int(x) for x in lines]

        def get_three(expense_report):
            for i in range(len(expense_report)):
                for j in range(i+1, len(expense_report)):
                    for k in range(j+1, len(expense_report)):
                        if expense_report[i]+expense_report[j]+expense_report[k]==2020:
                            return(expense_report[i]*expense_report[j]*expense_report[k])

        return get_three(lines)

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()