class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        l_max = s_max = nums[0]
        for i in range(1,len(nums)):
            s_max = max(s_max+nums[i],nums[i])
            l_max = max(s_max,l_max)
        return l_max