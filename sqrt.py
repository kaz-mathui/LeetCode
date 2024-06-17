# 計算量の詳細:

# 二分探索の原理:

# 二分探索は、探索範囲を半分に分割していくアルゴリズムです。これにより、各ステップで探索範囲が半分に減少します。
# 探索範囲が n から始まる場合、範囲が 1 になるまでに最大で log_2 n 回の比較が必要です。
# 初期範囲の設定:

# このアルゴリズムでは、平方根を求める対象の数 x の範囲を 2 から x // 2 に設定しています。これは、探索範囲が実際には x の値によって最大 log_2 (x // 2) 回の比較が必要になることを意味します。
# 計算量の結論:

# よって、全体の計算量は O(log x) となります。これは、探索範囲の上限が x に依存するためです。


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 2, x // 2
        
        while left <= right:
            mid = (left + right) // 2
            num = mid * mid
            
            if num > x:
                right = mid - 1
            elif num < x:
                left = mid + 1
            else:
                return mid
        
        return right

def test_mySqrt():
    sol = Solution()
    
    # テストケース1: 入力が4の場合
    assert sol.mySqrt(4) == 2, "Test case 1 failed"
    
    # テストケース2: 入力が8の場合
    assert sol.mySqrt(8) == 2, "Test case 2 failed"
    
    # テストケース3: 入力が0の場合
    assert sol.mySqrt(0) == 0, "Test case 3 failed"
    
    # テストケース4: 入力が1の場合
    assert sol.mySqrt(1) == 1, "Test case 4 failed"
    
    # テストケース5: 入力が16の場合
    assert sol.mySqrt(16) == 4, "Test case 5 failed"
    
    # テストケース6: 入力が2147395599の場合
    assert sol.mySqrt(2147395599) == 46339, "Test case 6 failed"
    
    print("All test cases pass")

# テスト実行
test_mySqrt()
