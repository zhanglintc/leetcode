# House Robber
# for leetcode problems
# 2015.04.16 by zhanglin

# Problem:
# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint stopping you from
# robbing each of them is that adjacent houses have security system connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.

# Credits:
# Special thanks to @ifanchu for adding this problem and creating all test cases.
# Also thanks to @ts for adding additional test cases.

class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        fina_max = 0
        for offset in range(len(num)):
            fina_max = max(fina_max, self.doRob(num, offset, num[offset]))

        return fina_max

    def doRob(self, num, offset, loot):
        if offset == (len(num) - 1) or offset == (len(num) - 2):
            return loot

        this_max = 0
        for offset in range(offset + 2, len(num)):
            this_max = max(this_max, self.doRob(num, offset, loot + num[offset]))

        return this_max


num = [2,1,1,2]

s = Solution()
print "\nlast: " + str(s.rob(num))


