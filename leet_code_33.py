from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n  = len(nums)
        alpha = []
        for i in range(n):
            alpha.append((i,nums[i]))

        for index,val in alpha:
            if(val == target):
                return index

        return -1

s = Solution()
nums = [4,5,6,7,0,1,2]
target = 3
print(s.search(nums,target))


        

        