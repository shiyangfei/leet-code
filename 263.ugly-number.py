#
# [263] Ugly Number
#
# https://leetcode.com/problems/ugly-number
#
# Easy (39.00%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '-2147483648'
#
# 
# Write a program to check whether a given number is an ugly number.
# 
# 
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# For example, 6, 8 are ugly while 14 is not ugly since it includes another
# prime factor 7.
# 
# 
# 
# Note that 1 is typically treated as an ugly number.
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):
    def is_valid(self, num):
        num = int(num)
        if num == 1:
            return True
        factors = [2, 3, 5]
        has_prime_factor = False
        for index, factor in enumerate(factors):
            if num % factor == 0:
                has_prime_factor = True
                num = num / factor
                break
        if has_prime_factor is False:
            return False
        else:
            return self.is_valid(num)

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        if num < 1:
            return False
        return self.is_valid(num)
