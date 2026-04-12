class Solution:
    def __init__(self):
        self.prefixes = {}

    def insert(self, word: str) -> None:
        curr_prefixes = self.prefixes
        for char in word:
            if char not in curr_prefixes:
                curr_prefixes[char] = {}
                curr_prefixes[char]["words"] = []
            if len(curr_prefixes[char]["words"]) < 3:
                curr_prefixes[char]["words"].append(word)
            curr_prefixes = curr_prefixes[char]

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        #---- build trie ---
        products.sort()
        for pr in products:
            self.insert(pr)
        res =[[]]*len(searchWord)
        # --- prefix search for each letter ---
        curr = self.prefixes
        for i in range(len(searchWord)):
            char = searchWord[i]
            if char not in curr:
                return res
              
            res[i] = curr[char]["words"]
            curr = curr[char]
        return res