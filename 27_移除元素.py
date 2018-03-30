class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        length,index = len(nums),0
        for i in nums:
            if i != val:
                nums[index] = i
                index += 1 
            else:
                length -= 1
        nums = nums[:length]
        return length