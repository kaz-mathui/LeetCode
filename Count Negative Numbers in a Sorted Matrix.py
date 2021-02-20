class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            if grid[i][len(grid[i])-1] >= 0:
                continue
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    ans += len(grid[i]) - j
        
                    break
        lists = list(itertools.chain.from_iterable(grid))
        print(lists)
        return ans
