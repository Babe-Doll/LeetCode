class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -10<x<10 :
            return(x)
        b = str(x)
        if b[0] == '-':
            b = b[1:][::-1]
            b = -int(b)
            if b < -2147483647:
                return 0
            else:
                return(b)
        else:
            b = b[::-1]
            b = int(b)
            if b > 2147483647:
                return 0
            else:
                return(b)
