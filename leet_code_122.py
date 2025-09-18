from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        big = 0
        small = 0
        summ = 0

        for i in range(len(prices)-1):
            if(prices[i]<prices[i+1]):
                small = prices[i]
                big = prices[i+1]
                summ= abs(small-big)
                profit += summ
        return profit        

s = Solution()
price = [7,1,5,3,6,4]
print(s.maxProfit(price))


        
