class Solution:
    def isPalindrome(self, s: str) -> bool:
        # すべての大文字を小文字に変換し、非英数字を取り除く
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        
        # リストの前後を比較して回文かどうかを確認する
        return filtered_chars == filtered_chars[::-1]

# 計算量の説明:
# 1. 大文字を小文字に変換し、非英数字を取り除く操作にはO(n)の時間がかかります。
# 2. リストの前後を比較する操作にもO(n)の時間がかかります。
# したがって、全体の時間計算量はO(n)となります。ここでnは文字列の長さです。

# 単体テスト
def test_solution():
    solution = Solution()

    # テストケース1: 一般的な回文のケース
    assert solution.isPalindrome("A man, a plan, a canal: Panama") == True, "Error in test case 1"

    # テストケース2: 回文ではないケース
    assert solution.isPalindrome("race a car") == False, "Error in test case 2"

    # テストケース3: 空文字列のケース
    assert solution.isPalindrome(" ") == True, "Error in test case 3"

    print("すべてのテストケースが成功しました。")

# テストの実行
test_solution()
