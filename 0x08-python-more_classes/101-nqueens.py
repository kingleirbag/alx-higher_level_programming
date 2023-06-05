#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.
"""


from sys import argv

if __name__ == "__main__":
    answer = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    count = int(argv[1])
    if count < 4:
        print("N must be at least 4")
        exit(1)

    """ initialize the answer list"""
    for i in range(count):
        answer.append([i, None])

    def if_queen_exists(y):
        """check that a queen does not already exist in that y value"""
        for x in range(count):
            if y == answer[x][1]:
                return True
        return False

    def reject_sol(x, y):
        """Reject the solution"""
        if (if_queen_exists(y)):
            return False
        i = 0
        while(i < x):
            if abs(answer[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_ans(x):
        """clears the answers from the point x to count of failure on"""
        for i in range(x, count):
            answer[i][1] = None

    def nqueens(x):
        """recursive backtracking function to find the solution"""
        for y in range(count):
            clear_ans(x)
            if reject_sol(x, y):
                answer[x][1] = y
                if (x == count - 1):
                    print(answer)
                else:
                    nqueens(x + 1)

    nqueens(0)
