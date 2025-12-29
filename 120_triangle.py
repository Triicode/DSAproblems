class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        length = len(triangle)
        for i in range(1,length):
            for j in range(len(triangle[i])):
                if j>0:
                    left = j-1
                else:
                    left = j
                if j<len(triangle[i])-1:
                    right = j+1
                else:
                    right = j
                triangle[i][j]+=min(triangle[i-1][left:right])


        return min(triangle[length-1])