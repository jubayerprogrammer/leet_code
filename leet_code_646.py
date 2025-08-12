from math import inf
from typing import List
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        before_right = -inf
        count = 0

        for left,right in pairs:
            if(left>before_right):
            
                count+= 1
                before_right = right

        return count       

    

               

          
      

        
    


s = Solution()
pairs =  [[1,2],[2,3],[3,4]]
print(s.findLongestChain(pairs))

        