import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    for i in lines:
        print("Hello {0}!".format(i))

if __name__ == '__main__':
    lines = []
    for l in input():
        lines.append(l.rstrip('\r\n'))
    main(lines)
