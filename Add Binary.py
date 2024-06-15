# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         return bin(int(a,2) + int(b,2))[2:]

# 計算量の詳細
# このアルゴリズムの計算量を分析すると、以下のようになります：

# 時間計算量 (Time Complexity):

# 主に影響する操作はバイナリ文字列の各桁ごとの和を計算する部分です。両方のバイナリ文字列の長さを n とすると、各桁を処理するために O(n) の時間がかかります。
# ゼロパディングと最終結果の反転と結合も、それぞれ O(n) の時間がかかります。
# したがって、全体の時間計算量は O(n) です。
# 空間計算量 (Space Complexity):

# 使用する追加のスペースは結果を格納するためのリストであり、これも最大で n + 1 (キャリーを考慮) なので、O(n) の空間を使用します。
# また、ゼロパディングされた新しい文字列 a と b も最大 n の長さです。
# したがって、全体の空間計算量は O(n) です。
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 2つのバイナリ文字列の長さを揃えるために、短い方に0をパディングする
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        print(a,b)
        carry = 0
        result = []
        
        # 右から左に向かって各桁を処理する
        for i in range(max_len - 1, -1, -1):
            print(i)
            total_sum = carry
            total_sum += int(a[i])
            total_sum += int(b[i])
            
            # 現在の桁の結果を計算
            result.append(str(total_sum % 2))
            carry = total_sum // 2
        
        # 最後にキャリーが残っている場合は追加
        if carry:
            result.append('1')
        
        # 結果を逆順にして結合し、最終結果とする
        return ''.join(result[::-1])

# 単体テスト
def test_addBinary():
    sol = Solution()
    
    # テストケース1
    assert sol.addBinary("11", "1") == "100"
    
    # テストケース2
    assert sol.addBinary("1010", "11111011") == "100000101"
    
    # その他のテストケース
    assert sol.addBinary("0", "0") == "0"
    assert sol.addBinary("1", "0") == "1"
    assert sol.addBinary("1111", "1111") == "11110"

    print("すべてのテストケースが通過しました。")

# テストの実行
test_addBinary()
