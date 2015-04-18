// Insertion Sort List
// for leetcode problems
// 2015.04.17 by zhanglin

// Problem Link:
// https://leetcode.com/problems/insertion-sort-list/

// Problem:
// Sort a linked list using insertion sort.

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode insertionSortList(ListNode head) {
        if(head == null) {
            return head;
        }

        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode insertPos = null;
        ListNode tobeMoved = null;

        ListNode current = head;
        while(current.next != null) {
            if(current.val < current.next.val) {
                current = current.next;
            }

            else {
                insertPos = dummy;
                while(insertPos.next.val < current.next.val) {
                    insertPos = insertPos.next;
                }

                tobeMoved = current.next;
                current.next = current.next.next;
                tobeMoved.next = insertPos.next;
                insertPos.next = tobeMoved;
            }
        }

        return dummy.next;
    }
}


