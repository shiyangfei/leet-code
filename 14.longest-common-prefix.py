#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (34.64%)
# Total Accepted:    633.6K
# Total Submissions: 1.8M
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
        assert strs is not None
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        res = ""
        curr = 1
        while True:
            if curr > len(strs[0]):
                return res
            temp_res = strs[0][0:curr]
            for item in strs:
                if not item.startswith(temp_res):
                    return res
            res = temp_res
            curr += 1
