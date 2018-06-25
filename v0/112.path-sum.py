#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum
#
# Easy (33.61%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\n1'
#
# 
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
# 
# 
# For example:
# Given the below binary tree and sum = 22,
# 
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \      \
# ⁠       7    2      1
# 
# 
# 
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, node, cur_sum, sum):
        if node.left is None and node.right is None:
            return node.val == sum - cur_sum
        else:
            cur_sum = cur_sum + node.val
            left_child_answer = False
            if node.left is not None:
                left_child_answer = self.helper(node.left, cur_sum, sum)
            right_child_answer = False
            if node.right is not None:
                right_child_answer = self.helper(node.right, cur_sum, sum)
            return left_child_answer or right_child_answer

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        return self.helper(root, 0, sum)
