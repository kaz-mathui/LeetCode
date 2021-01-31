class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = {}
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                # dic = {nums1[i]+nums2[j]:[nums1[i],nums2[j]]}
                result[[nums1[i],nums2[j]]] = nums1[i]+nums2[j]
        print(result)