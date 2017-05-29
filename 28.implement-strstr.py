#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr
#
# Easy (27.69%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '""\n""'
#
# 
# Implement strStr().
# 
# 
# Returns the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
# 
#
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None:
            return -1
        len_h = len(haystack)
        len_n = len(needle)
        if len_n > len_h:
            return -1
        for i in range(len_h - len_n + 1):
            j = 0
            while j < len_n:
                if haystack[j + i] != needle[j]:
                    break
                j += 1
            if j == len_n:
                return i
        return -1
