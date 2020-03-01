#
# @lc app=leetcode id=202 lang=python
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (48.34%)
# Total Accepted:    329.2K
# Total Submissions: 677.7K
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number is "happy".
# 
# A happy number is a number defined by the following process: Starting with
# any positive integer, replace the number by the sum of the squares of its
# digits, and repeat the process until the number equals 1 (where it will
# stay), or it loops endlessly in a cycle which does not include 1. Those
# numbers for which this process ends in 1 are happy numbers.
# 
# Example: 
# 
# 
# Input: 19
# Output: true
# Explanation: 
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 
#
class Solution(object):
    def get_digits(self, n):
        res = []
        while n > 0:
            digit = n % 10
            res.insert(0, digit)
            n = n // 10
        return res

    def calc(self, digits):
        res = 0
        for d in digits:
            res = res + d ** 2
        return res

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        trace = set()
        digits = self.get_digits(n)
        res = self.calc(digits)
        while True:
            if res == 1:
                return True
            digits = self.get_digits(res)
            res = self.calc(digits)
            if res in trace:
                return False
            trace.add(res)
