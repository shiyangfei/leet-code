#
# @lc app=leetcode id=38 lang=python
#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Easy (42.89%)
# Total Accepted:    351.8K
# Total Submissions: 819.7K
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers with the first five
# terms as following:
# 
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# 
# Given an integer n where 1 ≤ n ≤ 30, generate the n^th term of the
# count-and-say sequence. You can do so recursively, in other words from the
# previous member read off the digits, counting the number of digits in groups
# of the same digit.
# 
# Note: Each term of the sequence of integers will be represented as a
# string.
# 
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "1"
# Explanation: This is the base case.
# 
# 
# Example 2:
# 
# 
# Input: 4
# Output: "1211"
# Explanation: For n = 3 the term was "21" in which we have two groups "2" and
# "1", "2" can be read as "12" which means frequency = 1 and value = 2, the
# same way "1" is read as "11", so the answer is the concatenation of "12" and
# "11" which is "1211".
# 
# 
#
class Solution(object):
    # is n always positive int

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1 or n > 30:
            raise Exception('invalid n')
        return self.helper('1', 1, n)

    def helper(self, v, index, target):
        if index == target:
            return v
        elif index < target:
            output = self.read(v)
            return self.helper(output, index + 1, target)
        else:
            raise Exception('index is larger than target. something is wrong.')

    @staticmethod
    def read(v):
        count = 0
        last = None
        res = ''
        for c in v:
            if last is None:
                count = 1
            elif last == c:
                count += 1
            else:
                res += str(count) + last
                count = 1
            last = c
        res += str(count) + last
        return res
