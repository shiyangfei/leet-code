#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (33.91%)
# Total Accepted:    493.7K
# Total Submissions: 1.4M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
# 
# Example 1:
# 
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "race a car"
# Output: false
# 
# 
#
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        while left <= right:
            left_c = s[left]
            right_c = s[right]
            if not left_c.isalnum():
                left += 1
                continue
            if not right_c.isalnum():
                right -= 1
                continue
            if left_c.lower() != right_c.lower():
                return False
            left += 1
            right -= 1
        return True
