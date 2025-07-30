# https://leetcode.com/problems/valid-sudoku/description/

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # boards = [[[]] * 3] * 3 # This generates a shallow list!
        boards = [[[] for _ in range(3)] for _ in range(3)]
        rows = [[] for _ in range(9)]
        columns = [[] for _ in range(9)]

        for row, values in enumerate(board):
            for column, number in enumerate(values):
                if number == ".":
                    continue
                cell = boards[row // 3][column // 3]
                # "if number in (cell, rows[row], columns[column])" -  also works!
                if any(number in collection for collection in [cell, rows[row], columns[column]]):
                    return False

                cell.append(number)
                rows[row].append(number)
                columns[column].append(number)

        return True


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    board2 = [
        [".", ".", "4", ".", ".", ".", "6", "3", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["5", ".", ".", ".", ".", ".", ".", "9", "."],
        [".", ".", ".", "5", "6", ".", ".", ".", "."],
        ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
        [".", ".", ".", "7", ".", ".", ".", ".", "."],
        [".", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]

    solution = Solution()
    solution.isValidSudoku(board)
    solution.isValidSudoku(board2)
