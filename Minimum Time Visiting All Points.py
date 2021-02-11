class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        sec = 0
        x1,y1 = points.pop()
        while points:
            x2,y2 = points.pop()
            sec += max(abs(x1-x2),abs(y1-y2))
            x1,y1 = x2,y2
        return sec
            
        