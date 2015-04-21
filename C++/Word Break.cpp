// Word Break
// for leetcode problems
// 2015.04.11 by zhanglin

// Problem Link:
// https://leetcode.com/problems/word-break/

// Problem:
// Given a string s and a dictionary of words dict,
// determine if s can be segmented into a space-separated sequence of one or more dictionary words.

// For example, given
// s = "leetcode",
// dict = ["leet", "code"].

// Return true because "leetcode" can be segmented as "leet code".

class Solution {
public:
    bool wordBreak(string s, unordered_set<string> &dict) {
        bool dp[s.size() + 1] = {};
        dp[0] = true;

        for(int i = 0; i < s.size() + 1; i++) {
            for(int j = 0; j < i; j++) {
                if(dp[j] && dict.find(s.substr(j, i - j)) != dict.end()) {
                    dp[i] = true;
                }
            }
        }

        return dp[s.size()];
    }
};


