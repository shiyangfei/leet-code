#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs
#
# Easy (39.35%)
# Total Accepted:    166985
# Total Submissions: 424406
# Testcase Example:  '1'
#
# You are climbing a stair case. It takes n steps to reach to the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# 
# Note: Given n will be a positive integer.
# 
#
class Solution(object):
    def climbStairs(self, input_val):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        count_of_1 = input_val
        count_of_2 = 0
        while count_of_2 * 2 <= input_val / 2:
            result += choose(count_of_1 + count_of_2, count_of_2)
            count_of_2 += 1
            count_of_1 -= 1
        return result


def choose(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
