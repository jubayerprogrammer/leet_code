class Solution:
    def isPalindrome(self, s: str) -> bool:
        mark = []
        alpha = []
        for i in s:
            mark.append(i)

        for i in mark:
            if(ord(i)<= 47 and ord(i) >= 33):
                alpha.append(i)
            elif(ord(i)<=64 and ord(i)>=58):
                alpha.append(i)    
            elif(ord(i)<=96 and ord(i)>=91):
                alpha.append(i)
            elif(ord(i)<=126 and ord(i)>=123):
                alpha.append(i)  



        for i in alpha:
            mark.remove(i)

        word = ""
        for i in mark:
            word += i


        word_2 = word.split()


        word_3 = ""
        for i in word_2:
            word_3 += i


        word_4 = word_3.lower()
        n = len(word_4)
        mark.clear()


        for i in range(n-1,-1,-1):
            mark.append(word_4[i])   


        for i in range(n):
            if(mark[i] != word_4[i]):
                return False
            
        return True 



s = Solution()
str = "0p"
print(ord("0"))
print(s.isPalindrome(str))
        