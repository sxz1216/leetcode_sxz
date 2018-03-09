class Solution():
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_32 = 2**31
        i = 0
        num = 0
        if x >= 0 and x <= max_32-1:
            for w in str(x):
                num += int(w)*10**i
                i += 1
        elif x >= -max_32 and x <0:
            x = -x
            for w in str(x):
                num += int(w)*10**i
                i += 1
            num = -num
        else:
            return 0
        if num >= -max_32 and num <= max_32-1:
            return num
        else:
            return 0