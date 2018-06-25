#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths
#
# Easy (37.68%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,2,3,null,5]'
#
# 
# Given a binary tree, return all root-to-leaf paths.
# 
# 
# For example, given the following binary tree:
# 
# 
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# 
# 
# All root-to-leaf paths are:
# ["1->2->5", "1->3"]
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def get_path(self, node):
        sub_paths = []
        if node.left:
            sub_paths += self.get_path(node.left)
        if node.right:
            sub_paths += self.get_path(node.right)
        if len(sub_paths) > 0:
            for index, path in enumerate(sub_paths):
                sub_paths[index] = str(node.val) + '->' + sub_paths[index]
            return sub_paths
        else:
            return [str(node.val)]

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        return self.get_path(root)
