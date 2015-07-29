# Palindrome Linked List
# for leetcode problems
# 2015.07.29 by zhanglin

# Problem Link:
# https://leetcode.com/problems/palindrome-linked-list/

# Problem:
# Given a singly linked list, determine if it is a palindrome.

# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if not head:
            return True

        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # only ONE node
        if not slow.next:
            return True

        # more than ONE node
        left  = head
        right = self.reverseList(slow.next)
        fixNode = right

        while right:
            if left.val != right.val:
                slow.next = self.reverseList(slow.next)
                return False

            left  = left.next
            right = right.next

            return True

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

s = Solution()
node = ListNode(1)
node.next = ListNode(1)
node.next.next = ListNode(2)
node.next.next.next = ListNode(1)
print s.isPalindrome(node)

