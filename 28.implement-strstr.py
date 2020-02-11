#
# @lc app=leetcode id=28 lang=python
#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (33.66%)
# Total Accepted:    569.8K
# Total Submissions: 1.7M
# Testcase Example:  '"hello"\n"ll"'
#
# Implement strStr().
# 
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
# 
# Example 1:
# 
# 
# Input: haystack = "hello", needle = "ll"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# 
# 
# Clarification:
# 
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
# 
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
# 
#
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needle_len = len(needle)
        if len(needle) == 0:
            return 0
        haystack_len = len(haystack)
        pointer_index = 0
        while haystack_len >= pointer_index + needle_len:
            needle_index = 0
            valid = True
            for c in needle:
                if c != haystack[pointer_index + needle_index]:
                    pointer_index += 1
                    valid = False
                    break
                needle_index += 1
            if valid:
                return pointer_index
        return -1
