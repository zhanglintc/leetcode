// Best Time to Buy and Sell Stock III
// for leetcode problems
// 2015.05.17 by zhanglin

// Problem Link:
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

// Problem:
// Say you have an array for which the i[th] element is the price of a given stock on day i.

// Design an algorithm to find the maximum profit. You may complete at most TWO transactions.

// Note:
// You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

public class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;

        if(prices.length == 0) {
            return profit;
        }

        int[]  first = new int[prices.length];
        int[] second = new int[prices.length];

        // O(n) time to find maximum profit for first transaction
        int lowest = prices[0];
        for(int i = 1; i < prices.length; i++) {
            lowest = prices[i] < lowest ? prices[i] : lowest;
            first[i] = prices[i] - lowest > first[i - 1] ? prices[i] - lowest : first[i - 1];
        }

        // O(n) time to find maximum profit for second transaction
        int highest = prices[prices.length - 1];
        for(int i = prices.length - 2; i >= 0; i--) {
            highest = highest > prices[i] ? highest : prices[i];
            second[i] = highest - prices[i] > second[i + 1] ? highest - prices[i] : second[i + 1];
        }

        // O(n) time to find maximum profit
        for(int i = 0; i < prices.length; i++) {
            profit = profit > first[i] + second[i] ? profit : first[i] + second[i];
        }

        return profit;
    }
}


