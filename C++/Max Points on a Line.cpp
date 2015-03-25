// Max Points on a Line
// for leetcode problems
// 2015.03.24 by zhanglin

// Problem:
// Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

/**
 * Definition for a point.
 * struct Point {
 *     int x;
 *     int y;
 *     Point() : x(0), y(0) {}
 *     Point(int a, int b) : x(a), y(b) {}
 * };
 */
class Solution {
public:
    int maxPoints(vector<Point> &points) {
        int max_counter = 0;    // final answer
        int cur_counter = 0;    // temp answer
        int this_point_max = 0; // max point on a line with out repeat point
        int samePoint = 1;      // how many same point

        map<pair<int, double>, int> counter;
        pair<int, double> line;
        double slope = 0;

        if((int)points.size() == 1)
            return 1;

        if((int)points.size() == 2)
            return 2;

        for(int i = 0; i < (int)points.size(); i++) {
            for(int j = 0; j < (int)points.size(); j++) {
                // this point, jump over
                if(i == j)
                    continue;

                // same point, samePoint++
                if(points[i].x == points[j].x && points[i].y == points[j].y) {
                    samePoint += 1;
                    continue;
                }

                // vertical, special process
                else if(points[i].x == points[j].x) {
                    slope = (double)INT_MAX;
                    line.first = i;
                    line.second  = slope;
                }

                // other cases, not the same point
                else {
                    slope = (double)(points[i].y - points[j].y) / (double)(points[i].x - points[j].x);
                    line.first = i;
                    line.second  = slope;
                }

                // calculate the numbers of points on the same line
                counter[line] = (counter.find(line) == counter.end() ? 0 : counter.find(line)->second) + 1;

                // keep this_point_max as the max of this point
                this_point_max = this_point_max > counter[line] ? this_point_max : counter[line];
            }

            // calculate cur_counter
            cur_counter = this_point_max + samePoint;

            // update max_counter
            max_counter = max_counter > cur_counter ? max_counter : cur_counter;

            // reset this_point_max
            this_point_max = 0;

            // clean the counter
            counter.clear();

            // reset samePoint
            samePoint = 1;
        }

        return max_counter;
    }
};


