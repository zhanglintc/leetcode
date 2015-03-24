// Max Points on a Line
// for leetcode problems
// 2015.03.24 by zhanglin

// Problem:
// Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

/**
 * Definition for a point.
 * class Point {
 *     int x;
 *     int y;
 *     Point() { x = 0; y = 0; }
 *     Point(int a, int b) { x = a; y = b; }
 * }
 */
public class Solution {
    public int maxPoints(Point[] points) {
        int max_counter = 0;    // final answer
        int cur_counter = 0;    // temp answer
        int this_point_max = 0; // max point on a line with out repeat point
        int samePoint = 1;      // how many same point

        HashMap<Map, Integer> counter = new HashMap<Map, Integer>();
        HashMap<Integer, Double> line = new HashMap<Integer, Double>();
        double slope = 0.0;

        if(points.length == 1)
            return 1;

        if(points.length == 2)
            return 2;

        for(int i = 0; i < points.length; i++) {
            for(int j = 0; j< points.length; j++) {
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
                    slope = Double.MAX_VALUE;
                    line.put(i, slope);
                }

                // other cases, not the same point
                else {
                    slope = (double)(points[i].y - points[j].y) / (double)(points[i].x - points[j].x);
                    line.put(i, slope);
                }

                // calculate the numbers of points on the same line
                counter.put(line, (counter.get(line) == null ? 0 : counter.get(line)) + 1);

                // keep this_point_max as the max of this point
                this_point_max = Math.max(this_point_max, counter.get(line));
            }

            // calculate cur_counter
            cur_counter = this_point_max + samePoint;

            // update max_counter
            max_counter = Math.max(max_counter, cur_counter);

            // reset this_point_max
            this_point_max = 0;

            // clean the counter
            counter.clear();

            // reset samePoint
            samePoint = 1;
        }

        return max_counter;
    }
}


