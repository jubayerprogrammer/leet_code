from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        mark = []
        n = len(matrix)
        for i in range(n-1,-1,-1):
            mark.append(matrix[i])
        matrix.clear()    

        count = 0
        while(count <n):
            val  = []
            
            for i in range(n):
                val.append(mark[i][count])
                if not val in matrix:
                    matrix.append(val)
            count+=1
        print(matrix)

s = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
s.rotate(matrix)