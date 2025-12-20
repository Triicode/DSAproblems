class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        n=""
        for i in range(length-1,-1,-1):
            if n=="":
                if s[i]==" ":
                    continue
                else:
                    n+=s[i]
            else:
                if s[i]==" ":
                    break
                else:
                    n+=s[i]
        return len(n)