# Product of Array Except Self
# for leetcode problems
# 2015.07.27 by zhanglin

# Problem Link:
# https://leetcode.com/problems/product-of-array-except-self/

# Problem:
# Given an array of n integers where n > 1, nums,
# return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Solve it without division and in O(n).

# For example, given [1, 2, 3, 4], return [24, 12, 8, 6].

# Follow up:
# Could you solve it with constant space complexity?
# (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        output = []
        p = 1
        for i in range(len(nums)):
            output.append(p)
            p *= nums[i]

        p = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= p
            p *= nums[i]

        return output


