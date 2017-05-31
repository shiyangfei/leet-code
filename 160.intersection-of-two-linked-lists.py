#
# [160] Intersection of Two Linked Lists
#
# https://leetcode.com/problems/intersection-of-two-linked-lists
#
# Easy (30.40%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  'No intersection: []\n[]'
#
# Write a program to find the node at which the intersection of two singly
# linked lists begins.
# 
# For example, the following two linked lists: 
# 
# A:          a1 → a2
# ⁠                  ↘
# ⁠                    c1 → c2 → c3
# ⁠                  ↗            
# B:     b1 → b2 → b3
# 
# begin to intersect at node c1.
# 
# Notes:
# 
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function
# returns. 
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
# 
# 
# 
# Credits:Special thanks to @stellari for adding this problem and creating all
# test cases.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        if headA is headB:
            return headA
        listA = []
        listB = []
        while True:
            if headA is None:
                break
            listA.append(headA)
            headA = headA.next
        while True:
            if headB is None:
                break
            listB.append(headB)
            headB = headB.next
        if listA[-1] is not listB[-1]:
            return None
        lengthA = len(listA)
        lengthB = len(listB)
        minLength = min(lengthA, lengthB)
        for i in range(1, minLength + 1):
            if listA[-i] is not listB[-i]:
                return listA[-i + 1]
            if i == minLength:
                return listA[-i]
