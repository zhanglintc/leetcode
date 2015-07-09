# House Robber II
# for leetcode problems
# 2015.07.03 by zhanglin

# Problem Link:
# https://leetcode.com/problems/house-robber-ii/

# Problem:
# Note: This is an extension of House Robber.

# After robbing those houses on that street,
# the thief has found himself a new place for his thievery so that he will not get too much attention.
# This time, all houses at this place are arranged in a circle.
# That means the first house is the neighbor of the last one. Meanwhile,
# the security system for these houses remain the same as for those in the previous street.

# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.

# Credits:
# Special thanks to @Freezen for adding this problem and creating all test cases.

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        planA = self.rob_no_circle(nums[:-1])
        planB = self.rob_no_circle(nums[1:])

        return max(planA, planB)

    def rob_no_circle(self, num):
        if not num:
            return 0

        if len(num) == 1:
            return num[0]

        if len(num) == 2:
            return max(num[0], num[1])

        dp = [0 for i in range(len(num))]

        dp[0] = num[0]
        dp[1] = max(num[0], num[1])

        for i in range(2, len(num)):
            dp[i] = max(dp[i - 1], dp[i - 2] + num[i])

        return dp[-1]


