#
# [235] Lowest Common Ancestor of a Binary Search Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
#
# Easy (38.79%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[2,1]\nnode with value 2\nnode with value 1'
#
# 
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of
# two given nodes in the BST.
# 
# 
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes v and w as the lowest node in T that has both v
# and w as descendants (where we allow a node to be a descendant of
# itself).”
# 
# 
# 
# ⁠       _______6______
# ⁠      /              \
# ⁠   ___2__          ___8__
# ⁠  /      \        /      \
# ⁠  0      _4       7       9
# ⁠        /  \
# ⁠        3   5
# 
# 
# 
# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another
# example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of
# itself according to the LCA definition.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def has_child_node(self, node, child):
        if node is None:
            return False
        if node is child or node.left is child or node.right is child:
            return True
        return self.has_child_node(node.left, child) or self.has_child_node(node.right, child)

    def get_lca(self, node, p, q):
        if node.left and self.has_child_node(node.left, p) and self.has_child_node(node.left, q):
            return self.get_lca(node.left, p, q)
        elif node.right and self.has_child_node(node.right, p) and self.has_child_node(node.right, q):
            return self.get_lca(node.right, p, q)
        else:
            return node


    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.get_lca(root, p, q)
