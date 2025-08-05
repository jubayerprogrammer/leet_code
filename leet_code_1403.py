from typing import List
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        mark = []
        while(True):
            if(sum(mark)>sum(nums)):
                return mark
            
            max_val = max(nums)
            mark.append(max_val)
            nums.remove(max_val)



s = Solution()
nums = [4,4,7,6,7]
print(s.minSubsequence(nums))


        