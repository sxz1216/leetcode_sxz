class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n > 0:
        	rest = (n-1)%26
        	res = chr(rest+65) + res
        	n = int((n-1)/26)
        return res

s = Solution()
print(s.convertToTitle(701))