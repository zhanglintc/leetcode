# Reverse Linked List
# for leetcode problems
# 2015.07.01 by zhanglin

# Problem Link:
# https://leetcode.com/problems/reverse-linked-list/

# Problem:
# Reverse a singly linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head:
            return

        dummy_head = ListNode(0)
        dummy_head.next = head

        # set the three pointer
        headPrev = dummy_head
        headNext = head.next

        # do reverse
        while head.next:
            head.next = headPrev
            headPrev = head
            head = headNext
            headNext = headNext.next

        # reconnect three linked list
        head.next = headPrev
        dummy_head.next.next = headNext
        dummy_head.next = head

        return dummy_head.next


