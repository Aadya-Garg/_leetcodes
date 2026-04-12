class TrieNode:
    __slots__ = ["prefixes", "isEnd"]
    def __init__(self):
        self.prefixes = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, index: int = 0) -> None:
        curr = self.root
        for char in word:
            # if char not in curr.prefixes:
            #     curr.prefixes[char] = Trie()
            curr = curr.prefixes.setdefault(char, TrieNode()) #curr.prefixes[char]
        curr.isEnd = True

    def search(self, word: str, index: int = 0) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.prefixes:
                return False
            curr = curr.prefixes[char]
        return curr.isEnd

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