import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        c = collections.Counter(nums).most_common()
        # print(c.keys())
        
        for i in range(k):
            # print(c[k])
            result.append(c[i][0])
        return result