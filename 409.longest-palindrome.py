#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome
#
# Easy (45.29%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"abccccdd"'
#
# Given a string which consists of lowercase or uppercase letters, find the
# length of the longest palindromes that can be built with those letters.
# 
# This is case sensitive, for example "Aa" is not considered a palindrome
# here.
# 
# Note:
# Assume the length of given string will not exceed 1,010.
# 
# 
# Example: 
# 
# Input:
# "abccccdd"
# 
# Output:
# 7
# 
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# 
# 
#
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        # create a dict with char as key and count as value
        c_map = dict()
        has_single_char = False
        for index, c in enumerate(s):
            if c not in c_map:
                c_map[c] = 0
            c_map[c] += 1
        for key in c_map:
            if c_map[key] % 2 == 1:
                c_map[key] -= 1
                has_single_char = True
            result += c_map[key]
        if has_single_char:
            result += 1
        return result