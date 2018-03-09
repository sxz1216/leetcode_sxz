class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) > 1:
            for i in range(1,len(strs)):
                l1 = len(strs[0])
                l2 = len(strs[i])
                MIN = 0
                if l1 > l2:
                    MIN = l2
                else:
                    MIN = l1
                strs[0] = strs[0][:MIN]
                for j in range(MIN):
                    if strs[0][j] != strs[i][j]:
                        strs[0] = strs[0][:j]
                        break
            if strs[0] == 1:
                return ""
            else:
                return strs[0]
        elif len(strs) == 1:
            return strs[0]
        else:
            return ""