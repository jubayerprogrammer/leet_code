class Solution:
    def mySqrt(self, x: int) -> int:
        val = 0
        i = 0
        while(True):
            if(val>= x):
                break
                
            
            i+=1
            val = i*i
            
        if(val ==x):
            return i
        elif(val>x):
            return i-1
          
          
    
s = Solution()
x = 8
print(s.mySqrt(x))
    




        