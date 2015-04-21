# Binary Tree Right Side View
# for leetcode problems
# 2015.04.20 by zhanglin

# Problem Link:
# https://leetcode.com/problems/binary-tree-right-side-view/

# Problem:
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# You should return [1, 3, 4].

# Credits:
# Special thanks to @amrsaqr for adding this problem and creating all test cases.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# see Binary Tree Level Order Traversal.py
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        dikt = {}
        self.levelOrder(root, 1, dikt)

        lst = []
        for i in dikt:
            lst.append(dikt[i][-1])

        return lst

    def levelOrder(self, root, dept, dikt):
        if root == None:
            return root

        if dept not in dikt:
            dikt[dept] = []
        
        dikt[dept].append(root.val)

        self.levelOrder(root.left,  dept + 1, dikt)
        self.levelOrder(root.right, dept + 1, dikt)


