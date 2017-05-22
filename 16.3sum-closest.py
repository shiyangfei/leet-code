# coding=utf-8
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest
#
# Medium (30.81%)
# Total Accepted:    123475
# Total Submissions: 400730
# Testcase Example:  '[0,0,0]\n1'
#
# Given an array S of n integers, find three integers in S such that the sum is
# closest to a given number, target. Return the sum of the three integers. You
# may assume that each input would have exactly one solution.
# 
# 
# ⁠   For example, given array S = {-1 2 1 -4}, and target = 1.
#
# ⁠   The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
#
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        diff_result = float("inf")
        result = None
        for i in range(0, length - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = length - 1
            while left < right:
                temp_sum = nums[left] + nums[right] + nums[i]
                diff = temp_sum - target
                if diff == 0:
                    result = temp_sum
                    return result
                else:
                    if abs(diff) < diff_result:
                        diff_result = abs(diff)
                        result = temp_sum
                if diff > 0:
                    right -= 1
                else:
                    left += 1
        return result


Solution().threeSumClosest([0, 2, 1, -3], 1)
