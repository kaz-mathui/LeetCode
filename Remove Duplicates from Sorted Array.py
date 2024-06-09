# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         nums[:] = sorted(set(nums))
#         return len(nums)


# def test(solution):
#     nums = [1, 1, 2]
#     expected_nums = [1, 2]
#     k = solution.removeDuplicates(nums)
#     assert k == len(
#         expected_nums
#     ), f"Test case failed: expected {len(expected_nums)}, got {k}"
#     print(f"Test case passed!")


# def main():
#     solution = Solution()
#     test(solution)


# if __name__ == "__main__":
#     main()


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # Two pointers approach
        write_index = 1
        
        for read_index in range(1, len(nums)):
            print("if前","read_index:",read_index,nums[read_index],"write_index:",write_index, nums[write_index-1])
            if nums[read_index] != nums[write_index - 1]:
                nums[write_index] = nums[read_index]
                print(nums[read_index], nums[write_index])
                print(nums)
                write_index += 1
        
        return write_index

def test(solution):
    nums = [0,0,1,1,1,2,2,3,3,4]
    expected_nums = [0,1,2,3,4]
    k = solution.removeDuplicates(nums)
    assert k == len(
        expected_nums
    ), f"Test case failed: expected {len(expected_nums)}, got {k}"
    print(f"Test case passed!")

def main():
    solution = Solution()
    test(solution)

if __name__ == "__main__":
    main()
