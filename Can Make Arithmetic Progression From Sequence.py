class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        print(arr)
        dif = 0
        dif = arr[0] - arr[1]
        for i in range(1,len(arr)):
            if dif == arr[i-1] - arr[i]:
                continue
            else:
                return False
        return True