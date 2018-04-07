class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        mid = x/2
        while True:
            if mid*mid < x:
                left = mid
            elif mid*mid > x:
                right = mid
            else:
                return int(mid)
            mid = (left+right)/2
            print(mid,right)
            if right - left < 0.00001:
                break
        return int(right)

s = Solution()
print(s.mySqrt(2147395599))
            