class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        volume = 0
        while i<j:
            if min(height[i],height[j])*(j-i)>volume:
                volume = min(height[i],height[j])*(j-i)
            if height[i]>height[j]:
                j-=1
            elif height[i]<=height[j]:
                i+=1
        return volume