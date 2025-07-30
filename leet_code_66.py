from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = ""
        for i in digits:
            result += str(i)

        result = int(result) +1
        result = str(result)
        digits.clear()
        for i in result :
            digits.append(int(i))

        return digits    



s = Solution()
n = [4,3,2,1]
print(s.plusOne(n))


