from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()

        # Step 1: Find all rows and cols that need to be zeroed
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Step 2: Set rows to zero
        for i in rows:
            for j in range(n):
                matrix[i][j] = 0

        # Step 3: Set cols to zero
        for j in cols:
            for i in range(m):
                matrix[i][j] = 0    
