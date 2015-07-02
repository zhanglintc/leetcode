# Implement Stack using Queues
# for leetcode problems
# 2015.07.03 by zhanglin

# Problem Link:
# https://leetcode.com/problems/implement-stack-using-queues/

# Problem:
# Implement the following operations of a stack using queues.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.

# Notes:
# You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
# You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
# Update (2015-06-11):
# The class name of the Java function had been updated to MyStack instead of Stack.

# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and all test cases.

class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.stk = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stk.append(x)

    # @return nothing
    def pop(self):
        if self.stk:
            self.stk.pop()
        else:
            pass

    # @return an integer
    def top(self):
        if self.stk:
            return self.stk[-1]
        else:
            pass

    # @return an boolean
    def empty(self):
        return self.stk == []


