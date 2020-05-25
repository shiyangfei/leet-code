#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (29.50%)
# Total Accepted:    1.5M
# Total Submissions: 5M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
# 
#
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        res = 1
        index_left = 0
        index_right = 1
        char_map = {s[0]: 0}
        while index_right < len(s):
            c = s[index_right]
            if char_map.get(c) is not None:
                repeat_c_index = char_map.get(c)
                new_index_left = repeat_c_index + 1
                for i in range(index_left, new_index_left):
                    c_to_delete = s[i]
                    del char_map[c_to_delete]
                index_left = new_index_left
            cur_len = index_right - index_left + 1
            res = res if res > cur_len else cur_len
            char_map[c] = index_right
            index_right += 1
        return res
