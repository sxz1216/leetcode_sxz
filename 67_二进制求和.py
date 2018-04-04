class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a,2)
        b = int(b,2)
        c = a + b
        c = bin(c)
        return c.replace('0b','')
 
s = Solution()
print(s.addBinary('0','0'))