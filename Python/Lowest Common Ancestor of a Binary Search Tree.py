# Lowest Common Ancestor of a Binary Search Tree
# for leetcode problems
# 2015.07.18 by zhanglin

# Problem Link:
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Problem:
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

# According to the definition of LCA on Wikipedia:
# "The lowest common ancestor is defined between two nodes v and w
# as the lowest node in T that has both v and w as descendants
# (where we allow a node to be a descendant of itself)."

#         _______6______
#        /              \
#     ___2__          ___8__
#    /      \        /      \
#    0      _4       7       9
#          /  \
#          3   5

# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6.
# Another example is LCA of nodes 2 and 4 is 2,
# since a node can be a descendant of itself according to the LCA definition.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return root

        pList = []
        qList = []

        this = root
        while this.val != p.val:
            pList.append(this.val)

            if this.val > p.val:
                this = this.left

            else:
                this = this.right

        pList.append(this.val)

        this = root
        while this.val != q.val:
            qList.append(this.val)

            if this.val > q.val:
                this = this.left

            else:
                this = this.right

        qList.append(this.val)

        CA = pList.pop(0) # enough
        CA = qList.pop(0) # useless
        while pList and qList:
            pPop = pList.pop(0)
            qPop = qList.pop(0)

            if pPop != qPop:
                return CA

            else:
                CA = pPop # enough
                CA = qPop # useless

        return CA


