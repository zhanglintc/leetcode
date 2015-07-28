# Power of Two
# for leetcode problems
# 2015.07.28 by zhanglin

# Problem Link:
# https://leetcode.com/problems/power-of-two/

# Problem:
# Given an integer, write a function to determine if it is a power of two.

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False

        while n != 1:
            if n % 2 == 1:
                return False

            n >>= 1

        return True


