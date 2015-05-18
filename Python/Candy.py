# Candy
# for leetcode problems
# 2015.05.17 by zhanglin

# Problem Link:
# https://leetcode.com/problems/candy/

# Problem:
# There are N children standing in a line. Each child is assigned a rating value.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?

class Solution:
    # @param {integer[]} ratings
    # @return {integer}
    def candy(self, ratings):
        candies = [1 for i in range(len(ratings))]

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1

        return sum(candies)


