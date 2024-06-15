# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         before = 0
#         for i in range(len(digits)):
#             before += digits[i] * 10 ** (len(digits)-i-1)
#             # print(before)
#         after = str(before + 1)
#         # print(after)
#         ans = []
#         for i in range(len(after)):
#             ans.append(int(after[i]))
#         return ans
    
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # 末尾から順に処理を行う
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        # 全ての桁が9だった場合、1桁多い配列を返す
        return [1] + digits

# 計算量の説明
# このアルゴリズムはO(n)の時間計算量を持っています。
# ここでnはdigits配列の長さです。最悪の場合、配列の全ての桁を1回ずつ確認する必要があります。
# また、空間計算量はO(1)です。なぜなら、入力配列以外に追加の空間をほとんど使用しないからです。
# ただし、全ての桁が9である場合、新しい配列を作成するため、O(n)の空間を必要とします。

# 単体テスト
def test_plusOne():
    sol = Solution()
    
    # テストケース1
    digits = [1, 2, 3]
    expected = [1, 2, 4]
    result = sol.plusOne(digits)
    assert result == expected, f"Test1 failed: {result} != {expected}"

    # テストケース2
    digits = [4, 3, 2, 1]
    expected = [4, 3, 2, 2]
    result = sol.plusOne(digits)
    assert result == expected, f"Test2 failed: {result} != {expected}"
    
    # テストケース3
    digits = [9]
    expected = [1, 0]
    result = sol.plusOne(digits)
    assert result == expected, f"Test3 failed: {result} != {expected}"

    # テストケース4
    digits = [9, 9, 9]
    expected = [1, 0, 0, 0]
    result = sol.plusOne(digits)
    assert result == expected, f"Test4 failed: {result} != {expected}"
    
    # テストケース5
    digits = [0]
    expected = [1]
    result = sol.plusOne(digits)
    assert result == expected, f"Test5 failed: {result} != {expected}"
    
    print("All tests passed!")

# テスト実行
test_plusOne()
