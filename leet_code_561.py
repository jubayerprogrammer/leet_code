from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        alpha = []
        nums.sort()
        n = len(nums)
        for i in range(n-1):
            alpha.append((nums[i],nums[i+1])) 

        nums.clear()
        nums = alpha[0::2] 
        result = 0   
         

        for i in nums:
            result += min(i)
        return result    
            


s = Solution()
nums = [1,4,3,2]
print(s.arrayPairSum(nums))