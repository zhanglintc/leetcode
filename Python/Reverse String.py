# Reverse String
# for leetcode problems
# 2016.08.07 by zhanglin

# Problem Link:
# https://leetcode.com/problems/reverse-string/

# Problem:
# Write a function that takes a string as input and returns the string reversed.

# Example:
# Given s = "hello", return "olleh".

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        s = list(s)
        for i in range(size / 2):
            s[i], s[size - 1 - i] = s[size - 1 - i], s[i]

        return ''.join(s)


