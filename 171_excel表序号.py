class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        for i in range(len(s)):
           n += 26**i*(ord(s[-1-i])-64)
        return n