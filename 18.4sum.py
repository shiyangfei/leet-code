#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (27.89%)
# Total Accepted:    165.3K
# Total Submissions: 592.5K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
# 
# Note:
# 
# The solution set must not contain duplicate quadruplets.
# 
# Example:
# 
# 
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 4:
            return []
        result = []
        nums.sort()
        candidates = dict()
        i = 0
        while i <= length - 4:
            j = i + 1
            while j <= length - 3:
                start, end = j + 1, length - 1
                while start < end:
                    cur_sum = nums[i] + nums[j] + nums[start] + nums[end]
                    if cur_sum == target:
                        candidates[(nums[i], nums[j], nums[start], nums[end])] = True
                        start += 1
                        end -= 1
                    elif cur_sum < target:
                        start += 1
                    else:
                        end -= 1
                j += 1
            i += 1
        for item in candidates:
            result.append(list(item))
        return result
