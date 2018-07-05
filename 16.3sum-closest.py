#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (32.05%)
# Total Accepted:    184.6K
# Total Submissions: 575.9K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
#
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        nums.sort()
        i = 0
        result = float('inf')
        diff = float('inf')
        while i < length:
            start, end = i + 1, length - 1
            while start < end:
                cur_sum = nums[i] + nums[start] + nums[end]
                cur_diff = cur_sum - target
                if cur_diff == 0:
                    return cur_sum
                if abs(cur_diff) < diff:
                    diff = abs(cur_diff)
                    result = cur_sum
                if cur_diff < 0:
                    start += 1
                else:
                    end -= 1
            i += 1
        return result

