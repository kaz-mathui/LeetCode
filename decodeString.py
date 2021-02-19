class Solution:
    def decodeString(self, s: str) -> str:
        stack,curNum,curStr = [],0,''
        for st in s:
            if st == "[":
                stack.append(curStr)
                print(curNum)
                stack.append(curNum)
                curStr = ""
                curNum = 0
            elif st == "]":
                num = stack.pop()
                preStr = stack.pop()
                curStr = preStr + num*curStr
            elif st.isdigit():
                curNum = curNum*10 + int(st)
                
            else:
                curStr += st
        return curStr
# Runtime: 20 ms, faster than 98.29% of Python3 online submissions for Decode String.
# Memory Usage: 13.9 MB, less than 5.77% of Python3 online submissions for Decode String.                