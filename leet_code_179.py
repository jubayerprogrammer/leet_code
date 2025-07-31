from typing  import List
from functools import cmp_to_key
class Solution:
    def compare(self,a,b):
        if(a+b>b+a):
            return -1
        elif(b+a>a+b):
            return 1
        else:
            return 0


    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str,nums))
        nums.sort(key=cmp_to_key(self.compare))

        result = ""
        for i in nums:
            result+= i

        if(result[0] == "0"):
            return result[0]
        else:
            return result


s = Solution()
nums = [0,0]
print(s.largestNumber(nums))