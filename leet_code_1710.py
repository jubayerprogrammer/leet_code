from typing import List
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1],reverse=True)
        result = 0

        for i ,j in boxTypes:
            if(truckSize>=i):
                truckSize -= i
                result += i*j
            else:
                result += truckSize*j
                break

        return result
    

s = Solution()
box_type = [[5,10],[2,5],[4,7],[3,9]]
truck = 10

print(s.maximumUnits(box_type,truck))



        