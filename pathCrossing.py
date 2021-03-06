class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        isVisited = {(0,0):True}
        for i in path:
            if i == 'N':
                y += 1
            elif i == 'E':
                x += 1
            elif i == 'S':
                y -= 1
            else:
                x -= 1
            if isVisited.get((x,y)):
                return True
            isVisited[(x,y)] = True
        return False
# Runtime: 24 ms, faster than 96.92% of Python3 online submissions for Path Crossing.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Path Crossing.