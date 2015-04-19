// Insertion Sort List
// for leetcode problems
// 2014.08.15 by zhanglin

// Problem Link:
// https://leetcode.com/problems/insertion-sort-list/

// Problem:
// Sort a linked list using insertion sort.

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *insertionSortList(ListNode *head) {
        if(!head) {
            return head;
        }

        ListNode *dummy = new ListNode(0);
        dummy->next = head;

        ListNode *insertPos = NULL;
        ListNode *tobeMoved = NULL;

        ListNode *current = head;
        while(current->next) {
            if(current->val < current->next->val) {
                current = current->next;
            }

            else {
                insertPos = dummy;
                while(insertPos->next->val < current->next->val) {
                    insertPos = insertPos->next;
                }

                tobeMoved = current->next;
                current->next = current->next->next;
                tobeMoved->next = insertPos->next;
                insertPos->next = tobeMoved;
            }
        }

        return dummy->next;
    }
};


