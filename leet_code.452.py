from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        n = len(points)

        count = 1
        right = points[0][1]
        for i in range(n):
            if(points[i][0]>right):
                count+=1
                right = points[i][1]     

        return count        


        
    
s = Solution()
nums = [[10,16],[2,8],[1,6],[7,12]]
print(s.findMinArrowShots(nums))

            
            