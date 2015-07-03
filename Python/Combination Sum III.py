# Combination Sum III
# for leetcode problems
# 2015.07.03 by zhanglin

# Problem Link:
# https://leetcode.com/problems/combination-sum-iii/

# Problem:
# Find all possible combinations of k numbers that add up to a number n,
# given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
# Ensure that numbers within the set are sorted in ascending order.

# Example 1:
# Input: k = 3, n = 7
# Output:
# [[1,2,4]]

# Example 2:
# Input: k = 3, n = 9
# Output:
# [[1,2,6], [1,3,5], [2,3,4]]

# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.

class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        this_lst = []
        fina_lst = []

        self.search(k, n, 1, 0, this_lst, fina_lst)

        return fina_lst

    def search(self, k, n, start, depth, this_lst, fina_lst):
        if depth == k and sum(this_lst) == n:
            fina_lst.append(this_lst[:])
            return

        for i in range(start, 9 + 1):
            if i not in this_lst:
                this_lst.append(i)
                self.search(k, n, i, depth + 1, this_lst, fina_lst)
                this_lst.pop()


