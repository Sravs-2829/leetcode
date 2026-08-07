class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ro=[set() for _ in range(9)]
        co=[set() for _ in range(9)]
        bo=[set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                num=board[r][c]
                if num==".":
                    continue
                if num in ro[r]:
                    return False
                ro[r].add(num)
                if num in co[c]:
                    return False
                co[c].add(num)
                box=(r//3)*3+(c//3)
                if num in bo[box]:
                    return False
                bo[box].add(num)
        return True    