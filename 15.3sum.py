#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (21.84%)
# Total Accepted:    344.2K
# Total Submissions: 1.6M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#
class Solution(object):
    def helper(self, nums, target, target_index):
        res = []
        processed_num = dict()
        num_map = dict()
        for i, num in enumerate(nums):
            if i <= target_index or processed_num.get(num):
                continue
            if num_map.get(target - num):
                unit_candidate = [target - num, num, -target]
                unit_candidate.sort()
                unit_candidate = tuple(unit_candidate)
                res.append(unit_candidate)
                processed_num[num] = True
                processed_num[target - num] = True
            num_map[num] = True
        return res

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        targets = dict()
        candidates = dict()
        for i, num in enumerate(nums):
            if targets.get(-num) is None:
                unit_candidates = self.helper(nums, -num, i)
                for item in unit_candidates:
                    if candidates.get(item) is None:
                        candidates[item] = True
                targets[-num] = True
        for item in candidates:
            res.append(list(item))
        return res
