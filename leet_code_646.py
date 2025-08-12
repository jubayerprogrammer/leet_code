from typing import List
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        n = len(pairs)
        mark = []
        count = 0
        for i in range(n-1):
            val = pairs[i]
            val2 = pairs[i+1]
            
            num2 = val[1]
            num4 = val2[1]
            if(num2< num4):
                count+= 1
                mark.extend([val,val2])

        alpha = mark[::2] 

        val_1 = pairs[n-1]
        val_2 = alpha[len(alpha)-1]
        mark_first = val_1[0]
        alpha_last = val_2[1]
        if(alpha_last<mark_first):
            alpha.append(val_1)

               

          
        return len(alpha)

        
    


s = Solution()
pairs =  [[1,2],[2,3],[3,4]]
print(s.findLongestChain(pairs))

        