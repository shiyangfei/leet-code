#
# [189] Rotate Array
#
# https://leetcode.com/problems/rotate-array
#
# Easy (24.28%)
# Total Accepted:    126190
# Total Submissions: 519623
# Testcase Example:  '[1]\n0'
#
# Rotate an array of n elements to the right by k steps.
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to
# [5,6,7,1,2,3,4]. 
# 
# Note:
# Try to come up as many solutions as you can, there are at least 3 different
# ways to solve this problem.
# 
# 
# [show hint]
# Hint:
# Could you do it in-place with O(1) extra space?
# 
# 
# Related problem: Reverse Words in a String II
# 
# Credits:Special thanks to @Freezen for adding this problem and creating all
# test cases.
#
class Solution(object):
    def reverse(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # TODO: need to revisit the edge cases of this problem. This is very difficult.
        length = len(nums)
        k = k % length
        self.reverse(nums, 0, length - 1 - k)
        self.reverse(nums, length - k, length - 1)
        self.reverse(nums, 0, length - 1)

