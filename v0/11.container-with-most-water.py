#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water
#
# Medium (36.30%)
# Total Accepted:    127646
# Total Submissions: 351597
# Testcase Example:  '[1,1]'
#
# Given n non-negative integers a1, a2, ..., an, where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container and n is at least 2.
# 
#
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        length = len(height)
        left = 0
        right = length - 1
        while left < right:
            area = calc_area(left, right, height)
            result = max(result, area)
            if height[right] >= height[left]:
                left += 1
            else:
                right -= 1
        return result


def calc_area(left, right, integers):
    height = min(integers[left], integers[right])
    return height * (right - left)

Solution().maxArea([1, 1])
