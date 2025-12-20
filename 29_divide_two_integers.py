class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        n = 1
        count = 0
        sign = 1
        if divisor==0:
            return 0
        if dividend<0 and divisor<0:
            sign = 1
            dividend*=-1
            divisor*=-1
        elif dividend<0:
            sign = -1
            dividend*=-1
        elif divisor<0:
            sign = -1
            divisor*=-1
        temp = divisor
        while dividend>=divisor:
            while dividend>=temp+temp:
                temp = temp + temp
                n = n + n
            dividend-=temp
            temp = divisor
            count+=n
            n = 1
        if -2**31>count*sign:
            return -2**31
        elif 2**31-1<count*sign:
            return 2**31-1
        
        return count*sign