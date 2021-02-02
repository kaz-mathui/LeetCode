# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
    
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
#         if not grid:
#             return 0
            
#         m = len(grid)
#         n = len(grid[0])
#         sum  = 0
#         max_area = 0
#         for i in range(m):
#             for j in range(n):
#                 area = 0
#                 if grid[i][j] == 0:
#                     continue
#                 elif grid[i][j] == 1:
#                     # print('tanaka',i,j)
#                     #sum up only once per chance of meeting "1"
#                     sum += 1
#                     stack = list()
#                     stack.append([i,j])
#                     grid[i][j] = 0
#                     # area += 1
#                     #visit each "1" in the adjacent area using a stack
#                     while len(stack) != 0:
#                         [p,q] = stack.pop()
#                         print(p,q,area)
#                         if not (grid[p][q] == 2):
#                             area += 1
#                         if p >= 1 and grid[p-1][q] == 1:
#                             stack.append([p-1,q])
#                         if p < m -1 and grid[p+1][q] == 1:
                            
#                             stack.append([p+1,q])
#                         if q >= 1 and grid[p][q-1] == 1:
#                             stack.append([p,q-1])
#                         if q < n - 1 and grid[p][q + 1] == 1:
#                             stack.append([p,q+1])
#                         #mark as visited
#                         grid[p][q] = 2
#                     max_area = max(max_area,area)
        
        
        
#         return max_area

# 別解

class Solution(object):
    def maxAreaOfIsland(self, grid):
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))