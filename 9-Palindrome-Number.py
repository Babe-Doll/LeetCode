class Solution:
    def isPalindrome(self, x):
         strx = str(x)
         length = len(strx)
         flag = True
         for i in range(len(strx)-1):
             if strx[i] != strx[length-1-i]:
                 flag = False
                 return flag
             else:
                 flag = True
         return flag
x = 0
a = Solution()  
print(a.isPalindrome(x))
