import collections

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        sorted_counts,removed_counts = sorted(Counter(arr).items(),key=lambda x: x[1]),0
        for keys,values in sorted_counts:
            if k >= values:
                k -= values
                removed_counts += 1
        return len(sorted_counts) - removed_counts
