class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplet = []
        length = len(nums) 
        x = 0
        y = length - 1
        num = sorted(nums)
        for i in range(length-1):
            if i>0 and num[i-1]==num[i]:
                continue
            y = length-1
            x= i + 1
            
            while x<y:
                s = num[x]+num[y]
                if s<-num[i]:
                    x+=1
                elif s>-num[i]:
                    y-=1
                else:
                    triplet.append([num[i],num[x],num[y]])
                    x+=1
                    y-=1
                    while x<length-1 and num[x-1]==num[x]:
                        x+=1
                    while y>0 and num[y]==num[y+1]:
                        y-=1
                    
        return triplet