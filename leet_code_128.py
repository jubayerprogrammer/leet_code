from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if(n == 0):
            return 0
        nums.sort()
        print(nums)
        count = 1
        mark = []
        
        for i in range(n-1):
            if(nums[i+1] - nums[i]  ==  1) :
                count += 1
            elif(nums[i+1] - nums[i] > 1):
                mark.append(count)
                count =1   
        mark.append(count)
        
        return max(mark)

s= Solution()
nums = [9,1,4,7,3,-1,0,5,8,-1,6]
print(s.longestConsecutive(nums))       
        