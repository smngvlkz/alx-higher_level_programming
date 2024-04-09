#!/usr/bin/python3
import sys

def solve_nqueens(n):
    def can_place(pos, ocuppied_positions):
        for i in range(len(ocuppied_positions)):
            if ocuppied_positions[i] == pos or \
                    ocuppied_positions[i] - i == pos - len(ocuppied_positions) or \
                    ocuppied_positions[i] + i == pos + len(ocuppied_positions):
                        return False
        return True

    def put_queen(ocuppied_positions, target_row, n):
        if target_row == n:
            result.append(ocuppied_positions)
            return
        for column in range(n):
            if can_place(column, ocuppied_positions):
                put_queen(ocuppied_positions + [column], target_row + 1, n)

    result = []
    put_queen([], 0, n)
    return result

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    results = solve_nqueens(n)

    for result in results:
        print([[i, result[i]] for i in range(n)])

if __name__ == "__main__":
    main()
