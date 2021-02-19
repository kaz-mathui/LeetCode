class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.element = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        inserted = self.element
        for tmp in word:
            if tmp not in inserted:
                inserted[tmp] = {}
            inserted = inserted[tmp]
        inserted["-"] = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        searched = self.element
        for tmp in word:
            if tmp not in searched:
                return False
            searched = searched[tmp]
        return "-" in searched


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        started = self.element
        for tmp in prefix:
            if tmp not in started:
                return False
            started = started[tmp]
        return True




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Runtime: 128 ms, faster than 94.63% of Python3 online submissions for Implement Trie (Prefix Tree).
# Memory Usage: 27.3 MB, less than 66.67% of Python3 online submissions for Implement Trie (Prefix Tree).

trie = Trie()

trie.insert("apple")
trie.search("apple")   
#  returns true
trie.search("app")
#  returns false
trie.startsWith("app")
# returns true
trie.insert("app")
trie.search("app")
# returns true
print(trie.element)