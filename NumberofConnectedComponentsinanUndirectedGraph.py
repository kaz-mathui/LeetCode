# test = {1:[0,2],2:[3,4],3:[2,3]}
# if 0 in test:
#     print(1)
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # 周りの頂点を全て訪れたことにする
        def dfs(i):
            seen[i] = 1
            if i in dic:
                for neighbor in dic[i]:
                    if seen[neighbor] == 0:
                        dfs(neighbor)
        
        dic = {}
        for e in edges:
#             辞書の中にリストを作る
            if e[0] not in dic:
                dic[e[0]] = [e[1]]
#             なければ追加
            else:
                dic[e[0]].append(e[1])
#             逆側の頂点からも辞書に登録
            if e[1] not in dic:
                dic[e[1]] = [e[0]]
            else:
                dic[e[1]].append(e[0])
        seen = [0]*n
        count = 0
        for i in range(n):
            if seen[i] == 0:
                count += 1
                dfs(i)
        return count