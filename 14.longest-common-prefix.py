#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (31.74%)
# Total Accepted:    292.1K
# Total Submissions: 920.3K
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        res = ''
        prefix_c = ''
        index = 0
        lens = []
        for item in strs:
            lens.append(len(item))
        min_len = min(lens)
        while index < min_len:
            for i, item in enumerate(strs):
                if i == 0:
                    prefix_c = item[index]
                if item[index] != prefix_c:
                    return res
            res += prefix_c
            index += 1
        return res
