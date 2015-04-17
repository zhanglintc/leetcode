// Problem Name Here
// for leetcode problems
// 2015.04.17 by zhanglin

// Problem:
// You are a professional robber planning to rob houses along a street.
// Each house has a certain amount of money stashed, the only constraint stopping you from
// robbing each of them is that adjacent houses have security system connected
// and it will automatically contact the police if two adjacent houses were broken into on the same night.

// Given a list of non-negative integers representing the amount of money of each house,
// determine the maximum amount of money you can rob tonight without alerting the police.

// Credits:
// Special thanks to @ifanchu for adding this problem and creating all test cases.
// Also thanks to @ts for adding additional test cases.

class Solution {
public:
    int rob(vector<int> &num) {
        int fina_max = 0;
        int tmp = 0;
        for(int offset = 0; offset < num.size(); offset++) {
            tmp = doRob(num, offset, num[offset]);
            fina_max = fina_max > tmp ? fina_max : tmp;
        }
    }

    int doRob(vector<int> &num, int offset, int loot) {
        if(offset == num.size() - 1 || offset == num.size() - 2) {
            return loot;
        }

        int this_max = 0;
        int tmp = 0;
        for(offset = offset + 2; offset < num.size(); offset++) {
            tmp = doRob(num, offset, loot + num[offset]);
            this_max = this_max > tmp ? this_max : tmp;
        }

        return this_max;
    }
};


