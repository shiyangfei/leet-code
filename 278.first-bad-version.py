#
# [278] First Bad Version
#
# https://leetcode.com/problems/first-bad-version
#
# Easy (25.04%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '1 version\n1 is the first bad version.'
#
# 
# You are a product manager and currently leading a team to develop a new
# product. Unfortunately, the latest version of your product fails the quality
# check. Since each version is developed based on the previous version, all the
# versions after a bad version are also bad. 
# 
# 
# 
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first
# bad one, which causes all the following ones to be bad.
# 
# 
# 
# You are given an API bool isBadVersion(version) which will return whether
# version is bad. Implement a function to find the first bad version. You
# should minimize the number of calls to the API.
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
import math
class Solution(object):
    def find_version(self, start, end):
        if start == end:
            return start
        test_version = math.floor((end + start) / 2)
        if not isBadVersion(test_version):
            if end == start + 1:
                return end
            else:
                start = test_version
                return self.find_version(start, end)
        else:
            if end == start:
                return end
            else:
                end = test_version
                return self.find_version(start, end)

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(self.find_version(1, n))
