class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        array = [1] * 26
        for e in sentence:
            if array[ord(e) - ord('a')] == 1:
                array[ord(e) - ord('a')] = 0
        if sum(array) == 0:
            return True
        else:
            return False