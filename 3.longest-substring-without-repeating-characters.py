#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (24.79%)
# Total Accepted:    508.5K
# Total Submissions: 2.1M
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
        length = len(s)
        start, end = 0, 0
        c_map = dict()
        while True:
            if end >= length:
                break
            c = s[end]
            if c_map.get(c) is None:
                c_map[c] = 0
            c_map[c] = c_map[c] + 1
            # when there is a dupe c, move start to right
            while c_map[c] > 1:
                c_map[s[start]] = c_map[s[start]] - 1
                start += 1
            new_length = end - start + 1
            result = result if new_length <= result else new_length
            end += 1
        return result
