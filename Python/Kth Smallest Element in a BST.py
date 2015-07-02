#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Kth Smallest Element in a BST
# for leetcode problems
# 2015.07.02 by zhanglin

# Problem Link:
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Problem:
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

# Note: 
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

# Hint:

# Try to utilize the property of a BST.
# What if you could modify the BST node's structure?
# The optimal runtime complexity is O(height of BST).
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        valList = []
        self.loadValue(root, valList)

        return valList[k - 1]

    def loadValue(self, root, valList):
        if not root:
            return

        self.loadValue(root.left,  valList)
        valList.append(root.val)
        self.loadValue(root.right, valList)


