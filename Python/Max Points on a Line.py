# Max Points on a Line
# for leetcode problems
# 2014.08.11 by zhanglin

# Problem Link:
# https://leetcode.com/problems/max-points-on-a-line/

# Problem:
# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        max_counter = 0
        cur_counter = 0
        this_point_max = 0
        samePoint = 1

        counter = {}
        line = ()

        # if numbers of points is not enough, return directly
        if len(points) == 1:
            return 1

        if len(points) == 2:
            return 2

        # go through the list of points
        for i in range(len(points)):
            for j in range(len(points)):
                # this point, jump over
                if i == j:
                    continue

                # same point, samePoint++
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    samePoint += 1
                    continue

                # vertical, special process
                elif points[i].x == points[j].x:
                    slope = 'x'
                    line = (i, slope)

                # other cases, not the same point
                else:
                    slope = float((points[i].y - points[j].y)) / float((points[i].x - points[j].x))
                    line = (i, slope)

                # calculate the numbers of points on the same line
                counter[line] = counter.get(line, 0) + 1

                # keep this_point_max as the max of this point
                this_point_max = max(this_point_max, counter[line])

            # calculate cur_counter
            cur_counter = this_point_max + samePoint

            # update max_counter
            max_counter = max(max_counter, cur_counter)

            # reset this_point_max
            this_point_max = 0

            # clean the counter
            counter = {}

            # reset samePoint
            samePoint = 1

        return max_counter


