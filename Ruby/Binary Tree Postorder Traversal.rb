# Binary Tree Postorder Traversal
# for leetcode problems
# 2015.04.10 by zhanglin

# Problem:
# Given a binary tree, return the postorder traversal of its nodes' values.

# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [3,2,1].

# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Integer[]}
def postorder_traversal(root)
    lst = []
    helper(root, lst)
    return lst
end

def helper(root, lst)
    if root != nil
        helper(root.left,  lst)
        helper(root.right, lst)
        lst.push(root.val)
    end
end


