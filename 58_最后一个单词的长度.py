class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        s = s.rstrip(' ')
        s = ' ' + s     #统一处理
        k = 0
        for i in s[::-1]:
            if i != ' ':
                k += 1
            else:
                return k
                break
        return 0
                