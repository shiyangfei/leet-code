class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        left = 0
        c_map = {}
        for index, c in enumerate(s):
            if c in c_map and c_map[c] >= left:
                left = c_map[c] + 1
            c_map[c] = index
            result = max(result, index - left + 1)
        return result
