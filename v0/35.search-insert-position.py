#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position
#
# Easy (39.37%)
# Total Accepted:    164861
# Total Submissions: 418785
# Testcase Example:  '[1]\n0'
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
# 
# You may assume no duplicates in the array.
# 
# 
# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0
# 
#
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if nums[0] > target:
            return 0
        for index, num in enumerate(nums):
            if num == target:
                return index
            if index >= 1:
                if nums[index - 1] < target < nums[index]:
                    return index
        return len(nums)
