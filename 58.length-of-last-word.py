#
# @lc app=leetcode id=58 lang=python
#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (32.44%)
# Total Accepted:    332.4K
# Total Submissions: 1M
# Testcase Example:  '"Hello World"'
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word (last word means the last
# appearing word if we loop from left to right) in the string.
# 
# If the last word does not exist, return 0.
# 
# Note: A word is defined as a maximal substring consisting of non-space
# characters only.
# 
# Example:
# 
# 
# Input: "Hello World"
# Output: 5
# 
# 
# 
# 
#
class Solution(object):
    # what if "a "
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        space = ' '
        if not s or len(s) == 0:
            return 0
        count = 0
        last_count = 0
        for c in s:
            if c == space:
                last_count = count if count > 0 else last_count
                count = 0
            else:
                count += 1
        return count if count > 0 else last_count
