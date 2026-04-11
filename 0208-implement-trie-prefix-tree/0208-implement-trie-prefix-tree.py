class Trie:

    def __init__(self):
        self.prefixes = {}

    def insert(self, word: str) -> None:
        if len(word) == 0:
            return

        if len(word) == 1 and word != "$":
            word += "$"

        if word[0] not in self.prefixes:
            # print(f"{word[0]} is not there...")
            self.prefixes[word[0]] = Trie() # we keep adding keys

        new = self.prefixes[word[0]]
        new.insert(word[1:])
            
    def search(self, word: str) -> bool:
        if len(word) == 0:
            return True
        if len(word) == 1 and word != "$":
            word += "$"
        if word[0] not in self.prefixes.keys():
            return False
        return self.prefixes[word[0]].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True
        if prefix[0] not in self.prefixes.keys():
            return False
        return self.prefixes[prefix[0]].startsWith(prefix[1:])



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)