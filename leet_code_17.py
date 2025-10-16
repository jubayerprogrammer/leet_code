from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        context = {
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6"  :["m","n","o"],
            "7"  :["p","q","r","s"],
            "8"  :["t","u","v"],
            "9"  :["w","x","y","z"],
            }
        n = len(digits)
        if(n == 1):
            return context[digits]
        elif(n==2):
            result = []
            val = ""
            for i in range(2):
                val_1 = digits[i]
                for j in context[val_1]:
                    for k in range(i+1,2):
                        val_3 = digits[k]
                        for l in context[val_3]:
                            val = j+l
                            result.append(val)
           
                return result
        else:
                
            result = []
            val = ""
            for i in range(2):
                val_1 = digits[i]
                for j in context[val_1]:
                    for k in range(i+1,2):
                        val_3 = digits[k]
                        for l in context[val_3]:
                            val = j+l
                            result.append(val)
                mark = []
                m = 2
                while(m<n):
                    val_4 = digits[m]
                    for i1 in result:
                        for j1 in context[ val_4]:
                            val_5 = i1+j1
                            mark.append(val_5)
                    m+= 1
                    result.clear()
                    result = mark.copy()
                    mark.clear()
                return result
                    


                            


s = Solution()
digits = "2345"
print(s.letterCombinations(digits))

            
        