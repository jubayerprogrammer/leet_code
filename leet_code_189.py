from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        try:
            n = len(nums)
            mark = []
            if(n == 0 or n == 1):
                return nums
            
            if(n<k):
                print("hi")
                count = 0
                for i in range(k):
                    temp = nums[n-1]
                    nums.insert(0,temp)

                n2 = len(nums)
                count = 0
                for i in range(n2-1,-1,-1):
                    if(count == abs(n-n2)):
                        break
                    nums.pop(i)
                    count+=1

                return nums    

            
        
            count = 0
            for i in range(n-1,-1,-1):
                if(count==k):
                    break
                mark.append(nums[i])
                count+=1

            for i in mark:
                nums.insert(0,i) 

            n2 = len(nums)
            count= 0
            for i in range(n2-1,-1,-1):
                if(count== k):
                    break
                nums.pop(i)
                count+=1
            print(nums) 
        except:
            return nums



s = Solution()
nums = [1,2,3]
print(s.rotate(nums,4))