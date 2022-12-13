class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(1,m):
            for j in range(n):
                temp = []
                for x in [-1,0,1]:
                    if 0 <= j + x < n:
                        temp.append(matrix[i][j] + matrix[i-1][j+x])
                matrix[i][j] = min(temp)
        return min(matrix[-1])
