# Swap Nodes in Pairs
# for leetcode problems
# 2014.09.22 by zhanglin

# Problem Link:
# https://leetcode.com/problems/swap-nodes-in-pairs/

# Problem:
# Given a linked list, swap every two adjacent nodes and return its head.

# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Your algorithm should use only constant space. You may not modify the values in the list,
# only nodes itself can be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy.next

        while fast and fast.next:
            # swap two nodes
            TobeMoved = fast.next
            fast.next = TobeMoved.next
            TobeMoved.next = fast
            slow.next = TobeMoved

            # move forward
            slow = fast
            fast = fast.next

        return dummy.next


