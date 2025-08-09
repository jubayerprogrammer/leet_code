from  typing import List
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        n = 0
        for i in nums:
            if(i<0):
                n+= 1

        if(n<=1):
            min_val = min(nums)
            min_val_1 = min_val

            for i in range(k):
                min_val = (-1)* (min_val)

            min_val_index = nums.index(min_val_1)
            nums.insert(min_val_index,min_val)
            nums.pop(min_val_index+1)
            return sum(nums)
        
        elif(n>=k):
            for i in range(k):
                min_val = min(nums)
                min_val_2 = (-1)*(min_val)
                min_val_index = nums.index(min_val)
                nums.insert(min_val_index,min_val_2)
                nums.pop(min_val_index+1)
            return sum(nums)
        else:
            neg_number = abs(n-k)
            for i in range(n):
                min_val = min(nums)
                min_val_2 = (-1)*(min_val)
                min_val_index = nums.index(min_val)
                nums.insert(min_val_index,min_val_2)
                nums.pop(min_val_index+1)

            for i in range(neg_number):
                val = min(nums)
                val_2 = (-1) *(val)
                val_2_index = nums.index(val)
                nums.insert(val_2_index,val_2)
                nums.pop(val_2_index+1) 

           

            return sum(nums)
        

s = Solution()
nums = [4,-1,-2,7,-3]
k = 5
print(s.largestSumAfterKNegations(nums,k))