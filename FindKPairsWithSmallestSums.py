# class Solution:
#     def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
#         result = {}
#         for i in range(len(nums1)):
#             for j in range(len(nums2)):
#                 # dic = {nums1[i]+nums2[j]:[nums1[i],nums2[j]]}
#                 result[[nums1[i],nums2[j]]] = nums1[i]+nums2[j]
#         print(result)
import heapq
def kSmallestPairs(nums1, nums2, k):
    min_heap = []
    # If either of the arrays are empty then return empty list
    if not nums1 or not nums2:
        return []
    # Add the first row of the sum matrix to the heap [fix i = 0 and move j, which is adds 3,5,7]
    for j in range(len(nums1)):
        heapq.heappush(min_heap, [nums1[0] + nums2[j], 0, j])
        # print(min_heap)
    pairs = []
    while min_heap and k > 0:
        # pop from heap, NB the heap uses the first value (nums1[0] + nums2[j]) to validate heap property.
        min_sum, i, j = heapq.heappop(min_heap)
        print(min_sum,i,j)
        # Now append the pairs that just popped out of the heap
        pairs.append([nums1[i], nums2[j]])
        # Now move to the next row (9,11,13) by increamenting the i by 1
        if i+1 < len(nums1):
            heapq.heappush(min_heap, [nums1[i+1] + nums2[j], i+1, j] )
        k-=1
    return pairs

# print(kSmallestPairs([1,7,11],[2,4,6],3))