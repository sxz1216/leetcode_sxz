class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        length,index,t = len(nums),1,nums[0]
        for i in nums[1:]:
            if i != t:
                nums[index] = i
                index += 1
                t = i
            else:
                length -= 1
        nums = nums[:length]
        return length,nums
                

s = Solution()
print(s.removeDuplicates([1,1,2,2]))