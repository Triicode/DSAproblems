class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums) - 1
        closest = nums[0]+nums[1]+nums[2]
        #x + y + z = target
        #x + y = target - z
        for i in range(length):
            sums = target - nums[i]
            left = i+1
            right = length
            while left<right:
                curr = nums[left] + nums[i]+ nums[right]
                if abs(target-closest)>abs(target-curr):
                    closest = curr
                if nums[left] + nums[right]>sums:
                    right-=1
                elif nums[left] + nums[right]<sums:
                    left+=1
                else:
                    return closest        
        return closest