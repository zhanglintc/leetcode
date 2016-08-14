# Sum of Two Integers
# for leetcode problems
# 2016.08.08 by zhanglin

# Problem Link:
# https://leetcode.com/problems/sum-of-two-integers/

# Problem:
# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

# Example:
# Given a = 1 and b = 2, return 3.

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        m = min(a, b)

        s = 0 # sum
        t = 0 # times
        c = 0 # carry
        while m:
            ca = a & 1
            cb = b & 1

            s |= ((ca ^ cb ^ c) << t)

            if (ca & cb == 1 and ca | cb == 1) or (c and ca | cb == 1):
                c = 1
            else:
                c = 0

            a >>= 1
            b >>= 1
            m >>= 1
            t += 1

        return s | (a << t) | (b << t) | (c << t)

s = Solution()
a = s.getSum(-1, 122)
print a


