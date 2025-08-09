class Solution:
    def addBinary(self, a: str, b: str) -> str:
        store_1 = int(a,base=2)
        store_2 = int(b,base=2)
        sum = bin(store_1+ store_2 )
        sum = str(sum)
        result = sum[2:]
        return result

    
s = Solution()
a = "1010"
b = "1011"
print(s.addBinary(a,b))


        








        
        