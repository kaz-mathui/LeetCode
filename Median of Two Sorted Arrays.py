class Solution:
    def obtain_kth_num(self, nums1, nums2, k):
        nums1_len, nums2_len = len(nums1), len(nums2)
        nums1 = [-2**31] + nums1 + [2**31-1]
        nums2 = [-2**31] + nums2 + [2**31-1]
        print(nums1,nums2)
        left, right = max(0, k-nums2_len), min(nums1_len, k)
        while left <= right:
            i = (left+right) // 2
            j = k - i
            if nums1[i] > nums2[j+1]:
                right = i - 1
            elif nums2[j] > nums1[i+1]:
                left = i + 1
            else:
                return max(nums1[i], nums2[j])

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums_len = len(nums1) + len(nums2)
        mid = self.obtain_kth_num(nums1, nums2, (nums_len+1)//2)
        if nums_len % 2 == 0:
            mid = (mid+self.obtain_kth_num(nums1, nums2, (nums_len+1)//2+1)) / 2.0
        return mid
