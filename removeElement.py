class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # nums配列内の val を取り除く
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


def main():
    solution = Solution()
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(solution.removeElement(nums, val))


if __name__ == "__main__":
    main()

