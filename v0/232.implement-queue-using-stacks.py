#
# [232] Implement Queue using Stacks
#
# https://leetcode.com/problems/implement-queue-using-stacks
#
# Easy (36.35%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["MyQueue","empty"]\n[[],[]]'
#
# 
# Implement the following operations of a queue using stacks.
# 
# 
# push(x) -- Push element x to the back of queue.
# 
# 
# pop() -- Removes the element from in front of queue.
# 
# 
# peek() -- Get the front element.
# 
# 
# empty() -- Return whether the queue is empty.
# 
# 
# Notes:
# 
# You must use only standard operations of a stack -- which means only push to
# top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may
# simulate a stack by using a list or deque (double-ended queue), as long as
# you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek
# operations will be called on an empty queue).
# 
# 
#
import collections
class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def top(self):
        return self.data[-1]

    def pop(self):
        top = self.top()
        del self.data[-1]
        return top

    def empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = Stack()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.push_helper(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack.top()

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.stack.empty()

    def push_helper(self, x):
        if self.stack.empty():
            self.stack.push(x)
            return
        else:
            pop = self.stack.pop()
            self.push_helper(x)
            self.stack.push(pop)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
