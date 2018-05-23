class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        while k != 0:
            nums.insert(0,nums[-1])
            del nums[-1]
            k -= 1
        return nums

    def another_solution(self,nums,k):
        k = k % len(nums)
        nums = nums[len(nums)-k:] + nums[:len(nums)-k]
        return nums

s = Solution()
print(s.another_solution([1,2,3,4,5,6,7],3))
print(s.rotate([1,2,3,4,5,6,7],3))