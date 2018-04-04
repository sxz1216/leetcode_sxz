class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ''
        if n == 1:
            return '1'
        result = '1'
        for k in range(1,n):
            result = self.docountAndSay(result)
        return result
        
        
    def docountAndSay(self,s):
        first = s[0]
        num = 0
        result =  ''
        for c in s:
            if c == first:
                num += 1
            else:
                result += (str(num) + first)
                first = c
                num = 1
        result += (str(num) + first)
        return result