#
# [374] Guess Number Higher or Lower
#
# https://leetcode.com/problems/guess-number-higher-or-lower
#
# Easy (34.92%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '10\n6'
#
# We are playing the Guess Game. The game is as follows: 
# 
# I pick a number from 1 to n. You have to guess which number I picked.
# 
# Every time you guess wrong, I'll tell you whether the number is higher or
# lower.
# 
# You call a pre-defined API guess(int num) which returns 3 possible results
# (-1, 1, or 0):
# 
# -1 : My number is lower
# ⁠1 : My number is higher
# ⁠0 : Congrats! You got it!
# 
# 
# Example:
# 
# n = 10, I pick 6.
# 
# Return 6.
# 
# 
#
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

import math
class Solution(object):
    def helper(self, start, end):
        if end == start:
            return end
        guess_num = int(math.floor((start + end) / 2))
        result = guess(guess_num)
        if result == 0:
            return guess_num
        elif result == 1:
            start = guess_num + 1
            return self.helper(start, end)
        else:
            end = guess_num - 1
            return self.helper(start, end)

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.helper(0, n)
