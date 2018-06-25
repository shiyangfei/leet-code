#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix
#
# Easy (31.15%)
# Total Accepted:    167592
# Total Submissions: 537942
# Testcase Example:  '[]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
#
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ''
        if len(strs) == 0:
            return result
        first_str = strs[0]
        for index, c in enumerate(first_str):
            c_pass = True
            for str in strs:
                try:
                    if str[index] != c:
                        c_pass = False
                        break
                except:
                    c_pass = False
                    break
            if c_pass is True:
                result += c
            else:
                return result
        return result
