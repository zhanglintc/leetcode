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

    cache = {}

    def diffWaysToCompute(self, input):
        ops = "+-*"
        lst = []

        if input in self.cache:
            return self.cache[input]

        for idx in range(len(input)):
            if input[idx] in ops:
                left  = self.diffWaysToCompute(input[:idx])
                right = self.diffWaysToCompute(input[idx + 1:])
                op = input[idx]

                for l in left:
                    for r in right:
                        lst.append(eval(str(l) + op + str(r)))

                self.cache[input] = lst

        # if there's only numbers
        if not lst:
            lst.append(int(input))

        return lst


