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
        int max_counter = 0;
        int cur_counter = 0;
        int this_point_max = 1;
        map<int, int> modifier;
        map<pair<int, int>, int> counter;
        pair<int, int> line;
        int slope = 0;

        if(points.size() == 1)
            return 1;

        if(points.size() == 2)
            return 2;

        for(int i = 0; i < points.size(); i++) {
            for(int j = 0; j < points.size(); j++) {
                if(i == j)
                    continue;

                if(points[i].x == points[j].x && points[i].y == points[j].y) {
                    modifier[i] = (modifier.find(i) == modifier.end() ? 1 : modifier.find(i)->second) + 1;
                    continue;
                }

                else if(points[i].x == points[j].x) {
                    slope = 0xffff;
                    line.first = i;
                    line.second  = slope;
                }

                else {
                    slope = float((points[i].y - points[j].y)) / float((points[i].x - points[j].x));
                    line.first = i;
                    line.second  = slope;
                }

                counter[line] = (counter.find(line) == counter.end() ? 0 : counter.find(line)->second) + 1;
                this_point_max = this_point_max > counter[line] ? this_point_max : counter[line];
            }

            cur_counter = this_point_max + (modifier.find(i) == modifier.end() ? 1 : modifier.find(i)->second);
            this_point_max = 1;

            max_counter = max_counter > cur_counter ? max_counter : cur_counter;

            counter.clear();
        }

        return max_counter;
    }
};


