#
# @lc app=leetcode id=70 lang=python
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (46.03%)
# Total Accepted:    567.8K
# Total Submissions: 1.2M
# Testcase Example:  '2'
#
# You are climbing a stair case. It takes n steps to reach to the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# Note: Given n will be a positive integer.
# 
# Example 1:
# 
# 
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# 
# 
# Example 2:
# 
# 
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# 
# 
#
class Solution(object):
    # what if n is 0
    # requirement for performance
    # OK to use recursion?
    def __init__(self):
        self.mem = {}

    def helper(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        a1 = self.helper(n - 1) if self.mem.get(n - 1) is None else self.mem.get(n - 1)
        self.mem[n - 1] = a1
        a2 = self.helper(n - 2) if self.mem.get(n - 2) is None else self.mem.get(n - 2)
        self.mem[n - 2] = a2
        return a1 + a2

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.helper(n)
