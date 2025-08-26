class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        mark = []
        for i in s:
            mark.append(i)
        alpha = []

        n = len(mark)
        for i in range(n):
            if(mark.count(mark[i])>1):
                mark.pop(i)
                mark.insert(i,"no")
        return mark         

          




       

a = Solution()
s =  "cbacdcbc"
print(a.removeDuplicateLetters(s))
            