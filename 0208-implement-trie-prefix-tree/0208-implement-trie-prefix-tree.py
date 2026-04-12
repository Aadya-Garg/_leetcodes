class TrieNode:
    __slots__ = ["prefixes"]
    def __init__(self):
        self.prefixes = {}
        # self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, index: int = 0) -> None:
        curr = self.root
        word += "$"
        for char in word:
            curr = curr.prefixes.setdefault(char, TrieNode())

    def search(self, word: str, index: int = 0) -> bool:
        curr = self.root
        word += "$"
        for char in word:
            if char not in curr.prefixes:
                return False
            curr = curr.prefixes[char]
        return True

    def startsWith(self, prefix: str, index: int = 0) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.prefixes:
                return False
            curr = curr.prefixes[char]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)