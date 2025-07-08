class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = rows
        count = 0
        transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                transposed_matrix[j][i] = grid[i][j]
                
        for i in grid:
            if i in transposed_matrix:
                count += transposed_matrix.count(i)
        print(transposed_matrix)
        return count
        