def uniquePaths(grid: List[List[int]]) -> int:
    m = len(grid)+1
    n = len(grid[0])+1
    result_list = []
    result_list.append([1] * n)
    for i in range(1,m):
        n_list = []
        n_list.append(1)
        for j in range(1,n):
            if grid[i-1][j-1] == 1:
                n_list.append(0)
            else:
                n_list.append(result_list[i-1][j]+n_list[j-1])
        result_list.append(n_list)
    return result_list[m-1][n-1]
    # if m == 1 or n == 1:
    #     return 1
        
    # return uniquePaths(m - 1, n) + uniquePaths(m, n - 1)

if __name__ == '__main__':
    print(uniquePaths(23,12))