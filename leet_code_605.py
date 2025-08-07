from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) ->bool:
        if(n == 0):
            return True
        
        if(len(flowerbed) == 1 and flowerbed[0] == 0):
            return True
        

        count = 0
        m = len(flowerbed)

        if((flowerbed[0] == 0 ) and flowerbed[1] == 0 ):
            count+= 1
            flowerbed.insert(0,1)
            flowerbed.pop(1)
        if ((flowerbed[m-1] == 0) and (flowerbed[m-2] == 0)):
            count += 1
            flowerbed.insert(m-1,1)
            flowerbed.pop(m)


        
        for i in range(1,m-1):
            if((flowerbed[i]== 0) and (flowerbed[i+1] ==0) and (flowerbed[i-1] == 0) ):
                flowerbed.insert(i,1)
                flowerbed.pop(i+1)
                count += 1



        if(n <= count):
            return True    
    
        return False        


       

s = Solution()
flowerbed = [0,0,0,0,1]
n = 2
print(s.canPlaceFlowers(flowerbed,n))

