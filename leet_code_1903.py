class Solution:
    def largestOddNumber(self, num: str) -> str:
        try:
            num1 = int(num[len(num) - 1])
            if (num1 % 2 != 0):
                return num

            alpha = []
            for i in num:
                alpha.append(int(i))
            count = 0
            big_odd_index = 0
            m = len(alpha)
            for i in range(m):
                if (alpha[i] % 2 != 0):
                    big_odd_index = i
                    count+=1
            if(count == 0):
                return ""

            word_2 = []
            for i in range(big_odd_index + 1):
                word_2.append(str(alpha[i]))

            result_2 = ""
            for i in word_2:
                result_2 += i


            result_2 = int(result_2)

            return str(result_2)
        except:
            return str(result_2)



s = Solution()
num = "547234678"
print(s.largestOddNumber(num))



