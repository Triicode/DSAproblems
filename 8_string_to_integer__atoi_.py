class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = "1234567890"
        num=""
        for i in s:
            if num=="":
                if i == "-":
                    num+=i
                    continue
                elif i == "+":
                    num+=i
                    continue
                elif i == " ":
                    continue
                elif i in nums:
                    num+=i
                else:
                    break
            else:
                if i not in nums:
                    break
                num+=i
        try:
            numb = int(num)
        except:
            return 0
        if -2**31<=numb<2**31:
            return numb
        elif -2**31>numb:
            return -2**31
        else:
            return 2**31-1