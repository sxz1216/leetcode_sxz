class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle or haystack == needle:
            return 0
        if not haystack:
            return -1
        if needle in haystack:
            for i in range(len(haystack)-len(needle)+1):
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1

'''
        return haystack.find(needle)
'''