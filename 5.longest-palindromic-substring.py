#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (28.67%)
# Total Accepted:    899.1K
# Total Submissions: 3.1M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#
class Solution(object):
    def get_palin(self, left, right, s, base):
        res = base
        while left >= 0 and right < len(s) and s[left] == s[right]:
            res = s[left] + res + s[right]
            left -= 1
            right += 1
        return res

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) <= 1:
            return s
        res = s[0]
        for i in range(0, len(s)):
            res_even = self.get_palin(i, i + 1, s, '')
            res_odd = self.get_palin(i - 1, i + 1, s, s[i])
            res_temp = res_odd if len(res_odd) > len(res_even) else res_even
            res = res if len(res) > len(res_temp) else res_temp
        return res
