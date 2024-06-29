from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 初期化 - すべての要素を1に設定
        row = [1] * (rowIndex + 1)

        # 1行目から始まり、各行の要素を更新
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                print(i,j)
                print(row)
                row[j] += row[j - 1]

        return row


# 計算量の詳細:
# 空間計算量: O(rowIndex)
# - 結果を保存するためにrowIndex + 1個の要素を持つリストを使用します。
# 時間計算量: O(rowIndex^2)
# - 各行の要素を計算するために二重ループを使用します。
# - 外側のループはrowIndex回繰り返し、内側のループは平均してrowIndex/2回繰り返します。


# 単体テスト
def test_solution():
    sol = Solution()

    # テストケース 1
    result = sol.getRow(3)
    assert result == [1, 3, 3, 1], f"expected [1, 3, 3, 1] but got {result}"

    # テストケース 2
    result = sol.getRow(0)
    assert result == [1], f"expected [1] but got {result}"

    # テストケース 3
    result = sol.getRow(1)
    assert result == [1, 1], f"expected [1, 1] but got {result}"

    # テストケース 4 (追加のテストケース)
    result = sol.getRow(4)
    assert result == [1, 4, 6, 4, 1], f"expected [1, 4, 6, 4, 1] but got {result}"

    print("全てのテストケースを通過しました！")


# テスト実行
test_solution()
