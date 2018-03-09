class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        i = 0
        num = 0
        if x >= 0:
            for w in str(x):
    	        num += int(w)*10**i
    	        i = i+1
        if x == num:
            return True
        else:
            return False