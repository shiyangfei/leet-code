#
# [404] Sum of Left Leaves
#
# https://leetcode.com/problems/sum-of-left-leaves
#
# Easy (46.84%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Find the sum of all left leaves in a given binary tree.
# 
# Example:
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# There are two left leaves in the binary tree, with values 9 and 15
# respectively. Return 24.
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, node, sum_val):
        if node is None:
            return sum_val
        else:
            if node.left and not node.left.left and not node.left.right:
                sum_val = sum_val + node.left.val
            sum_val = self.helper(node.left, sum_val)
            sum_val = self.helper(node.right, sum_val)
            return sum_val

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, 0)
