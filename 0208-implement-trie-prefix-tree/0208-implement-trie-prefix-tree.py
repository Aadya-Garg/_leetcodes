class Trie:

    def __init__(self):
        self.prefixes = {}
        self.isEnd = False

    def insert(self, word: str, index: int = 0) -> None:
        try:
            if word[index] not in self.prefixes:
                self.prefixes[word[index]] = Trie() # we keep adding keys

            self.prefixes[word[index]].insert(word, index + 1)
        except IndexError:
            self.isEnd = True
            return

    def search(self, word: str, index: int = 0) -> bool:
        try:
            if word[index] not in self.prefixes:
                return False

            return self.prefixes[word[index]].search(word, index+ 1)
        except IndexError:
            return self.isEnd

    def startsWith(self, prefix: str, index: int = 0) -> bool:
        try:
            if prefix[index] not in self.prefixes:
                return False
            return self.prefixes[prefix[index]].startsWith(prefix, index + 1)
        except IndexError:
            return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)