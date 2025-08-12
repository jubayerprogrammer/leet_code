from typing import List
from math import  inf

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:


        max_val  =-inf
        max_list = []
        for i in arrays:
            big_val = max(i)
            if (big_val > max_val):
                max_val = big_val
                max_list = i


        min_val = inf
        for i in arrays:
            small_val = min(i)
            if(i == max_list):
                continue

            if (small_val < min_val):
                min_val = small_val

        if(min_val == inf):
            min_val = max_val

        val1 = abs(min_val - max_val)
        result =[]
        result.append(val1)


        min_val2 = inf
        min_list2 = []
        for i in arrays:
            small_val2 = min(i)
            if(small_val2<min_val2):
                min_val2 = small_val2
                min_list2 = i


        max_val2 = -inf
        for i in arrays:
            big_val2 = max(i)
            if(i == min_list2):
                continue
            if(big_val2>max_val2):
                max_val2 = big_val2

        if(max_val2 == -inf):
            max_val2 = min_val2

        val2 = abs(max_val2 - min_val2)
        result.append(val2)
        return max(result)



s = Solution()
arrays = [[1],[1]]
print(s.maxDistance(arrays))

