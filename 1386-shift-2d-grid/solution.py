class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        total = m * n
        k %= total
        
        # Flatten the grid
        a = [num for row in grid for num in row]
        
        # Rotate the list
        a = a[-k:] + a[:-k]
        
        # Build the new grid
        new_grid = []
        for i in range(m):
            new_grid.append(a[i * n : (i + 1) * n])
        
        return new_grid
