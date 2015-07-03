# Remove Linked List Elements
# for leetcode problems
# 2015.07.03 by zhanglin

# Problem Link:
# https://leetcode.com/problems/remove-linked-list-elements/

# Problem:
# Remove all elements from a linked list of integers that have value val.

# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5

# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        if not head:
            return head

        dummy_head = ListNode(0)
        dummy_head.next = head

        headPrev = dummy_head

        while head:
            if head.val == val:
                headPrev.next = head.next
                head = head.next

            else:
                headPrev = headPrev.next
                head = head.next

        return dummy_head.next


