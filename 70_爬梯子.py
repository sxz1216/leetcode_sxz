class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 2
        if n == 1 or n == 2:
            return n
        else:
            for i in range(n-2):
                a,b = b, a+b
            return b