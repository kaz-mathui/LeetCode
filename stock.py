class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         result = 0
#         tmp = prices.copy()
#         for i in range(len(prices)):
#             tmp.remove(prices[i])
#             # print(tmp)
#             if tmp == []:
#                 max_price = 0
#             else:
#                 max_price = max(tmp)
#             if result < max_price - prices[i]:
#                 result = max_price - prices[i]
#             if max_price <= result:
#                 break
#         if result < 0:
#             return 0
#         else:
#             return result
        
        min_price = 100000
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit