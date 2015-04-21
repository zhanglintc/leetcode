// Best Time to Buy and Sell Stock
// for leetcode problems
// 2015.03.23 by zhanglin

// Problem Link:
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

// Problem:
// Say you have an array for which the i[th] element is the price of a given stock on day i.

// If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock)
// design an algorithm to find the maximum profit.

public class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;

        if(prices.length == 0) {
            return profit;
        }

        int lowest = prices[0];

        for(int i = 1; i < prices.length; i++) {
            lowest = lowest < prices[i] ? lowest : prices[i];
            profit = profit > prices[i] - lowest ? profit : prices[i] - lowest;
        }

        return profit;
    }
}


