# public class Solution {
#     public int subarraySum(int[] nums, int k) {
#         int count = 0, sum = 0;
#         HashMap < Integer, Integer > map = new HashMap < > ();
#         map.put(0, 1);
#         for (int i = 0; i < nums.length; i++) {
#             sum += nums[i];
#             if (map.containsKey(sum - k))
#                 count += map.get(sum - k);
#             map.put(sum, map.getOrDefault(sum, 0) + 1);
#         }
#         return count;
#     }
# }

class Solution:
    def subarraySum(self, nums, k):
        preSums = {0: 1}
        s = 0
        res = 0
        for num in nums:
            s += num
            res += preSums.get(s - k, 0)
            preSums[s] = preSums.get(s, 0) + 1
        return res

# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         count = 0
#         for i in range(len(nums)):
#             sub_sum = 0
#             for j in range(i,len(nums)):
#                 sub_sum += nums[j]
#                 if sub_sum == k:
#                     count += 1
#         return count
