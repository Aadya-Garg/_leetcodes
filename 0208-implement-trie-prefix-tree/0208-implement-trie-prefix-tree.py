class Trie:

    def __init__(self):
        self.prefixes = {}
        self.isEnd = False

    def insert(self, word: str, index: int = 0) -> None:
        curr = self
        for char in word:
            if char not in curr.prefixes:
                curr.prefixes[char] = Trie()
            curr = curr.prefixes[char]
        curr.isEnd = True
        # try:
        #     if word[index] not in self.prefixes:
        #         self.prefixes[word[index]] = Trie() # we keep adding keys

        #     self.prefixes[word[index]].insert(word, index + 1)
        # except IndexError:
        #     self.isEnd = True
        #     return

    def search(self, word: str, index: int = 0) -> bool:
        curr = self
        for char in word:
            if char not in curr.prefixes:
                return False
            curr = curr.prefixes[char]
        return curr.isEnd

    def startsWith(self, prefix: str, index: int = 0) -> bool:
        curr = self
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