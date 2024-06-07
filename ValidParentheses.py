# O(n)の計算量
class Solution(object):
    def isValid(self, s: str) -> bool:
        # 辞書を閉じ括弧から開き括弧へマッピング
        bracket_map = {")": "(", "}": "{", "]": "["}
        # スタックをリストとして初期化
        stack = []

        for char in s:
            if char in bracket_map:
                # スタックが空でない場合はポップし、空の場合はダミー値
                top_element = stack.pop() if stack else None
                # マッピングが一致しなければ無効
                if bracket_map[char] != top_element:
                    return False
            else:
                # 開き括弧はスタックにプッシュ
                stack.append(char)

        # スタックが空であれば有効
        return not stack


def main():
    solution = Solution()
    print(solution.isValid("()"))  # Output: True
    print(solution.isValid("()[]{}"))  # Output: True
    print(solution.isValid("(]"))  # Output: False
    print(solution.isValid("([)]"))  # Output: False
    print(solution.isValid("{[]}"))  # Output: True


if __name__ == "__main__":
    main()
