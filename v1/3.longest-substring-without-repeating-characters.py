#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters
#
# Medium (24.09%)
# Total Accepted:    281519
# Total Submissions: 1168438
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# Examples:
# 
# Given "abcabcbb", the answer is "abc", which the length is 3.
# 
# Given "bbbbb", the answer is "b", with the length of 1.
# 
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the
# answer must be a substring, "pwke" is a subsequence and not a substring.
#
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        if len(s) == 0:
            return result
        c_map = dict()
        left = 0
        for index, c in enumerate(s):
            if c in c_map and left <= c_map[c]:
                left = c_map[c] + 1
            c_map[c] = index
            result = max(result, index - left + 1)
        return result
