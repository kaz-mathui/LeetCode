import numpy as np

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
#         intを文字列にしてからをリストに変換⇒各桁をリストに追加
        n_list = list(map(int,list(str(n))))
        return np.prod(n_list) - np.sum(n_list)
        
        # for s in range(len(n_string)):
        #     print(s)
        #     num_list.append(int(n_string[s])
        # print(num_list)
        # np_list = np.array(num_list)
        # print(np_list)
        # print(np.prod(np_list))
        # print(np.sum(np_list))
# import numpy as np

# class Solution:
#     def subtractProductAndSum(self, n):
#         l_n = list(map(int, list(str(n))))
#         print(list(str(n)))
#         return np.prod(l_n) - np.sum(l_n)