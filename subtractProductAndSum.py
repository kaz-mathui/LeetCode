# import numpy as np

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
#         intを文字列にしてからをリストに変換⇒各桁をリストに追加
        n_list = list(map(int,list(str(n))))
        prod = 1
        sum = 0
        for i in n_list:
            prod *= i
            sum += i
        return prod-sum
        # return np.prod(n_list) - np.sum(n_list)
        
       