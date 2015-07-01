# Contains Duplicate
# for leetcode problems
# 2015.06.30 by zhanglin

# Problem Link:
# https://leetcode.com/problems/contains-duplicate/

# Problem:
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False


