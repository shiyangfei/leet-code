# coding=utf-8
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum
#
# Medium (26.33%)
# Total Accepted:    114155
# Total Submissions: 433541
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array S of n integers, are there elements a, b, c, and d in S such
# that a + b + c + d = target? Find all unique quadruplets in the array which
# gives the sum of target.
# 
# Note: The solution set must not contain duplicate quadruplets.
# 
# 
# 
# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
#
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        result = []
        for i in range(0, length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target_1 = target - nums[i]
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                target_2 = target_1 - nums[j]
                left = j + 1
                right = length - 1
                while left < right:
                    if nums[left] + nums[right] == target_2:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                    elif nums[left] + nums[right] > target_2:
                        right -= 1
                    else:
                        left += 1
        return result


Solution().fourSum([0, 0, 0, 0], 0)
