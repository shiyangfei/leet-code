#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree
#
# Easy (46.01%)
# Total Accepted:    198372
# Total Submissions: 431115
# Testcase Example:  '[]\n[]'
#
# 
# Given two binary trees, write a function to check if they are equal or not.
# 
# 
# Two binary trees are considered equal if they are structurally identical and
# the nodes have the same value.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def nodes_none_check(self, node1, node2):
        if node1 is None and node2 is not None:
            return False
        if node1 is not None and node2 is None:
            return False
        return True

    def helper(self, node_p, node_q):
        if node_p is None and node_q is None:
            return True
        if self.nodes_none_check(node_p, node_q) is False:
            return False
        if node_p.val != node_q.val:
            return False
        else:
            if self.nodes_none_check(node_p.left, node_q.left) is False:
                return False
            if self.nodes_none_check(node_p.right, node_q.right) is False:
                return False
            return self.helper(node_p.left, node_q.left) and self.helper(node_p.right, node_q.right)

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.helper(p, q)
