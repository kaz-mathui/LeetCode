# class KthLargest:

#     def __init__(self, k: int, nums: list):
#         """
#         :param int k:
#         :param List[int] nums:
#         """
#         self.k = k
#         self.nums = nums

#     def add(self, val: int) -> int:
#         self.nums.append(val)
#         self.nums = sorted(self.nums, reverse=True)
#         return self.nums[self.k - 1]

# # Your KthLargest object will be instantiated and called as such:
# # obj = KthLargest(k, nums)
# # param_1 = obj.add(val)



import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.lists,self.num = [],k
        for i in nums:
            self.add(i)

    def add(self, val: int) -> int:
        heapq.heappush(self.lists, val)
        if len(self.lists) > self.num: 
            heapq.heappop(self.lists)
            # print(self.lists)
        return self.lists[0]
