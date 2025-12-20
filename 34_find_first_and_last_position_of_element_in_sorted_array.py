class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        length = len(nums)
        right = length - 1
        initial = -1
        final = -1
        n = length//2
        if length == 0:
            return [initial,final]
        while left<=right:
             
            n = left + (right-left)//2
            if nums[n]<target:
                left = n+1
            elif nums[n]>target:
                right = n-1
            elif nums[n]==target:
                initial = final = n
                while initial>=1 and nums[initial - 1] == target:
                    initial-=1
                while final<length-1 and nums[final + 1] == target:
                    final+=1
                break
        return [initial,final]