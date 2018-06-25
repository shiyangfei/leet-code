#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree
#
# Easy (38.05%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
# 
# 
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# But the following [1,2,2,null,3,null,3]  is not:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# Note:
# Bonus points if you could solve it both recursively and iteratively.
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

    def two_nodes_same(self, node_p, node_q):
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
            return self.two_nodes_same(node_p.left, node_q.left) and self.two_nodes_same(node_p.right, node_q.right)

    def flip_node(self, node):
        left_child = node.left
        right_child = node.right
        node.left = right_child
        node.right = left_child
        if node.left:
            node.left = self.flip_node(node.left)
        if node.right:
            node.right = self.flip_node(node.right)
        return node

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if is_none(root.left) != is_none(root.right):
            return False
        if root.left.val != root.right.val:
            return False
        return self.two_nodes_same(root.left, self.flip_node(root.right))


def is_none(node):
    return node is None
