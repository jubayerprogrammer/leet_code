from typing import List
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        mark = []
        n = len(s)
        for i in range(n) :
            mark.append(i)

        alpha = []
        for i in range(n):
            if(s[i] == "I"):
                min_val = min(mark)
                alpha.append(min_val)
                mark.remove(min_val)
            else:
                max_val = max(mark)
                alpha.append(max_val)
                mark.remove(max_val)
        return alpha        




        
        

n = Solution()
s =  "IDID"
print(n.diStringMatch(s))       
        