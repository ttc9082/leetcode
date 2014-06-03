# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points) < 3:
            return len(points)
        res = 0
        for i in xrange(len(points)):
            same_points = 1
            k_dict = {'inf': 0}
            for j in xrange(len(points)):
                if i == j:
                    continue
                if points[i].x == points[j].x and points[i].y != points[j].y:
                    k_dict['inf'] += 1
                elif points[i].x != points[j].x:
                    k = float(points[i].y - points[j].y) / (points[i].x - points[j].x)
                    try:
                        k_dict[k] += 1
                    except:
                        k_dict[k] = 1
                else:
                    same_points += 1
            res = max(res, max(k_dict.values()) + same_points)
        return res