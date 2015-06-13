# Invert Binary Tree
# for leetcode problems
# 2015.06.13 by zhanglin

# Problem Link:
# https://leetcode.com/problems/invert-binary-tree/

# Problem:
# Invert a binary tree.

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9

# to

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
# Google: 90% of our engineers use the software you wrote (Homebrew),
# but you cannot invert a binary tree on a whiteboard so fuck off.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if not root:
            return root

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


