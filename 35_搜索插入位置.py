class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        if target in nums:
            for v in nums:
                if target == v:
                    return i
                else:
                    i += 1
        else:
            for v in nums:
                if target > nums[-1]:
                    return len(nums)
                if target < v:
                    return i
                else:
                    i += 1
        