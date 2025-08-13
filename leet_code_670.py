
class Solution:
    def maximumSwap(self, num: int) -> int:
        mark = []
        num = str(num)
        for i in num:
            mark.append(int(i))
        mark_2 = mark.copy() 
           

        alpha = mark.copy()
        alpha.sort(reverse=True)
        num = int(num)

        if(mark == alpha):
            return num
        else:
            n = len(mark)
            for i in range(n):
                if(mark[i] != alpha[i]):
                    big_num = alpha[i]
                    mini_num = mark[i]
                    big_index = alpha.index(big_num)
                    mini_index = mark.index(mini_num)
                    break


            if(mark_2.count(big_num)>1):
                while(True):
                    if(mark_2.count(big_num) ==1 ):
                        break
                    big_index_2 = mark_2.index(big_num)
                    
                    mark_2.insert(big_index_2,None)
                    mark_2.pop(big_index_2+1)


            


            big_index_3 = mark_2.index(big_num)
            mini_index_3 = mark_2.index(mini_num)

            mark.insert(mini_index_3,big_num)
            mark.pop(mini_index_3+1)
            mark.insert(big_index_3,mini_num)
            mark.pop(big_index_3+1)

            
            num = ""
            
            for i in mark:
                num += str(i)

            num = int(num)
            return num

s = Solution()
num = 115
print(s.maximumSwap(num))            


        