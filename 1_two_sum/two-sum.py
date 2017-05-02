class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for index, num in enumerate(nums):
            if target - num in num_map:
                return [num_map[target - num], index]
            num_map[num] = index


# Solution().twoSum([3, 2, 4], 6)
