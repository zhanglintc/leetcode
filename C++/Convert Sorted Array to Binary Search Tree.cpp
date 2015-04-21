// Convert Sorted Array to Binary Search Tree
// for leetcode problems
// 2014.08.28 by zhanglin

// Problem Link:
// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

// Problem:
// Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode *sortedListToBST_helper(ListNode *head, TreeNode *root) {
        root->left  = new TreeNode(0);
        root->right = new TreeNode(0);
        ListNode *fast = head;
        ListNode *slow = head;
        ListNode *prev = head;

        ListNode *left  = NULL; // here
        ListNode *right = NULL; // here

        // no node
        if(head == NULL) {
            return NULL;
        }

        // one node
        if(head->next == NULL) {
            root->val = head->val;
            root->left  = NULL;
            root->right = NULL;
            return root;
        }

        // two nodes
        if(head->next->next == NULL) {
            root->val   = head->next->val;
            head->next  = NULL;
            root->left  = sortedListToBST_helper(head,  root->left);
            root->right = sortedListToBST_helper(NULL, root->right);
            return root;
        }

        // three or more nodes
        while(fast->next != NULL && fast->next->next != NULL) {
            fast = fast->next->next;
            prev = slow;
            slow = slow->next;
        }

        // odd
        if(fast->next == NULL) {
            left = head;
            right = slow->next;
            root->val = slow->val;
            prev->next = NULL;
        }

        // even
        else if(fast->next->next == NULL) {
            left = head;
            right = slow->next->next;
            root->val = slow->next->val;
            slow->next = NULL;
        }

        root->left  = sortedListToBST_helper(left,  root->left);
        root->right = sortedListToBST_helper(right, root->right);

        return root;
    }

    TreeNode *sortedListToBST(ListNode *head) {
        TreeNode *root = new TreeNode(0);
        return sortedListToBST_helper(head, root);
    }
};


