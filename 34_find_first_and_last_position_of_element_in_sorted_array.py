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
        if length == 0:
            return [initial,final]
        while left<=right:
            n = left + (right-left)//2
            if nums[n]<target:
                left = n+1
            elif nums[n]>target:
                right = n-1
            elif nums[n]==target:
                mid = r1 = n
                while left<=r1:
                    n = left + (r1 - left)//2
                    if nums[n]<target:
                        left = n+1
                    else:
                        r1 = n-1
                while mid<=right:
                    n = mid + (right - mid)//2
                    if nums[n]>target:
                        right = n-1
                    else:
                        mid = n + 1
                initial = left
                final = right
                break
        return [initial,final]