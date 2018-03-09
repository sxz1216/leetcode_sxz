class Solution(object):
    def twoSum(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for index,value in enumerate(nums):
            rest = target - value
            if rest in dic:
                return [dic[rest],index]
            else:
                dic[value] = index