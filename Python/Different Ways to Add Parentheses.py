# Different Ways to Add Parentheses
# for leetcode problems
# 2015.07.29 by zhanglin

# Problem Link:
# https://leetcode.com/problems/different-ways-to-add-parentheses/

# Problem:
# Given a string of numbers and operators,
# return all possible results from computing all the different possible ways to group numbers and operators.
# The valid operators are +, - and *.

# Example 1
# Input: "2-1-1".

# ((2-1)-1) = 0
# (2-(1-1)) = 2
# Output: [0, 2]

# Example 2
# Input: "2*3-4*5"

# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
# Output: [-34, -14, -10, -10, 10]

# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.

class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        lst = []
        nms = []
        ops = []
        tmp = ""

        for s in input:
            if s in "+-*":
                ops.append(s)
                nms.append(tmp)
                tmp = ""

            else:
                tmp += s

        nms.append(tmp)

        self.dfs(nms[:], ops[:], lst)

        return (lst)

    def dfs(self, nms, ops, lst):
        if not ops:
            lst.append(int(nms[0]))
            return

        for i in range(len(ops)):
            tmp = eval(nms[i] + ops[i] + nms[i + 1])

            if i == len(ops) - 1:
                self.dfs(nms[:i] + [str(tmp)], ops[:i] + ops[i + 1:], lst)

            else:
                self.dfs(nms[:i] + [str(tmp)] + nms[i + 2:], ops[:i] + ops[i + 1:], lst)

# input:
# "15-7*6+24"
# expect:
# [-195,-51,-3,72,240]
# result
# [72,240,-3,-51,240,-195]

s = Solution()
print s.diffWaysToCompute("2*3-4*5")

