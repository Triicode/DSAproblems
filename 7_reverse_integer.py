class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        y = ""
        f = str(x)
        if f[0]=="-":
            y+="-"
            for i in range(len(f)-1,0,-1):
                y+=f[i]
        else:
            for i in range(len(f)-1,-1,-1):
                y+=f[i]
        if -2**31<=int(y)<=2**31-1:
            return int(y)
        return 0