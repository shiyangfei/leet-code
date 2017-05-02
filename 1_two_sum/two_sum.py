class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = None
        num_map = dict()
        for index, num in enumerate(nums):
            lookfor = target - num
            if lookfor in num_map:
                result = [num_map[lookfor], index]
                break
            else:
                num_map[(target - num)] = index
        return result