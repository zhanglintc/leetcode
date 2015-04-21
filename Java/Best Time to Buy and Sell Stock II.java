// Best Time to Buy and Sell Stock II
// for leetcode problems
// 2015.03.25 by zhanglin

// Problem Link:
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

// Problem:
// Say you have an array for which the i[th] element is the price of a given stock on day i.

// Design an algorithm to find the maximum profit.
// You may complete as many transactions as you like
// (ie, buy one and sell one share of the stock multiple times). 
// However, you may not engage in multiple transactions at the same time
// (ie, you must sell the stock before you buy again).

public class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        boolean bought = false;

        for(int i = 0; i < prices.length - 1; i++) {
            if(prices[i] < prices[i + 1] && bought == false) {
                profit -= prices[i];
                bought = true;
            }

            if(prices[i] > prices[i + 1] && bought == true) {
                profit += prices[i];
                bought = false;
            }
        }

        if(bought == true) {
            profit += prices[prices.length - 1];
        }

        return profit;
    }
}


