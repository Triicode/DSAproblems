class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=1
        seen={}
        max_len=0
        left = 0
        length = 0
        for i in s:
            if i in seen:
                left = max(left,seen[i]+1)
                length = n - left
            seen[i]=n
            n+=1
            length+=1
            if max_len<length:
                max_len = length
        return max_len