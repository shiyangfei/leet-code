#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray
#
# Easy (39.24%)
# Total Accepted:    187188
# Total Submissions: 476988
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 
# Find the contiguous subarray within an array (containing at least one number)
# which has the largest sum.
# 
# 
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
# 
# 
# click to show more practice.
# 
# More practice:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#
class Solution(object):
    # empty array is not a subarray in this problem
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_val = 0
        max_sum = None

        for i in range(0, len(nums)):
            if sum_val < 0:
                sum_val = 0
            sum_val = sum_val + nums[i]
            if max_sum is None:
                max_sum = sum_val
            else:
                max_sum = max(sum_val, max_sum)
        return max_sum
