class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX = 2 ** 31
        sign = 1 if x >= 0 else -1
        x = abs(x)
        result = 0
        while x > 0:
            result = (10 * result) + x % 10
            if result > MAX:
                return 0
            x //= 10
        return result * sign