from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # パスカルの三角形を初期化
        triangle = []

        # 各行を生成
        for row_num in range(numRows):
            # 行の初期化。すべて1で初期化
            row = [1] * (row_num + 1)

            # 行の内部の要素を計算
            for j in range(1, row_num):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            # 現在の行を三角形に追加
            triangle.append(row)

        return triangle


# 計算量の説明
"""
計算量は以下の通りです：

時間計算量: O(numRows^2)
- 最初のforループはnumRows回繰り返されます。
- 各行の内部の要素を計算する内側のforループは、最長でnumRows-1回繰り返されます。
  従って、全体としては1 + 2 + 3 + ... + numRowsという計算を行うため、これはO(numRows^2)となります。

空間計算量: O(numRows^2)
- パスカルの三角形自体を格納するためのリストは、最悪の場合、numRows^2の要素を持つことになります。
"""

# 単体テスト
if __name__ == "__main__":
    solution = Solution()

    # テストケース1: numRows = 5
    assert solution.generate(5) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
    ]

    # テストケース2: numRows = 1
    assert solution.generate(1) == [[1]]

    # テストケース3: numRows = 3
    assert solution.generate(3) == [[1], [1, 1], [1, 2, 1]]

    print("すべてのテストケースが成功しました。")
