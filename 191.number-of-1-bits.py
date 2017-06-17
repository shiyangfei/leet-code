#
# [191] Number of 1 Bits
#
# https://leetcode.com/problems/number-of-1-bits
#
# Easy (39.29%)
# Total Accepted:    149497
# Total Submissions: 380453
# Testcase Example:  '           0 (00000000000000000000000000000000)'
#
# Write a function that takes an unsigned integer and returns the number of ’1'
# bits it has (also known as the Hamming weight).
# 
# For example, the 32-bit integer ’11' has binary representation
# 00000000000000000000000000001011, so the function should return 3.
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
import math
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = n
        count = 0
        while temp > 0:
            carry = temp % 2
            count += carry
            # TODO: need to be care of about python's int / float convert
            temp = int(math.floor(temp / 2))
        count += temp % 2
        return count

Solution().hammingWeight(1)
