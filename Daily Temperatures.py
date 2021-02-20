class Solution(object):
    def dailyTemperatures(self, T):
        ans,stack = [0] * len(T),[]
        for i, j in enumerate(T):
            # print(i,j)
            while stack and T[stack[-1]] < j:
                ans[stack.pop()] = i - stack[-1]
            stack.append(i)
            # print(ans)
        return ans
