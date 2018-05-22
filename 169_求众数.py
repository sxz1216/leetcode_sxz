class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rate = {}
        for i in nums:
            if i not in rate:
                rate[i] = 1
            else:
                rate[i] += 1
        for k,v in rate.items():
            if v > len(nums)/2:
                return k