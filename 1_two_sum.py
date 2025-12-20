class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x = len(nums)
        seen = {}
        for i in range(0,x):
            n = nums[i]
            need = target-n
            if need in seen:
                return [i,seen[need]]
            seen[n]=i