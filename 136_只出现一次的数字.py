class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        for i in range(int(len(nums)/2)):
            if nums[-1] != nums[-2]:
                return nums[-1]
            else:
                nums.pop()
                nums.pop()
        return nums[0]

s = Solution()
print(s.singleNumber([4,4,1,1,3,2,2,3,5]))