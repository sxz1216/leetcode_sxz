class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0
        while n > 4:
            n = int(n/5)
            num += n
        return num
s = Solution()
print(s.trailingZeroes(135))