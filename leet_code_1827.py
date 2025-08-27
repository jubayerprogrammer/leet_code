from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        alpha = []
        count= 0
        
        for i in range(len(nums)-1):
            result = 0
            if(nums[i] >=nums[i+1]):
                sub_val = (nums[i] - nums[i+1])+1
                result = sub_val + nums[i+1]
                count += result - nums[i+1]
                nums.insert(i+1,result)
                nums.pop(i+2)
                
                
        return count       
            

s= Solution()
nums =  [1,5,2,4,1]
print(s.minOperations(nums))
