class Solution:
    def __init__(self):
        self.prefixes = {"words": []}

    def insert(self, word: str, index: int = 0) -> None:
        curr_prefixes = self.prefixes
        for char in word:
            if char not in curr_prefixes:
                curr_prefixes[char] = {"words": []}

            if len(curr_prefixes[char]["words"]) < 3:
                curr_prefixes[char]["words"].append(index)

            curr_prefixes = curr_prefixes[char]

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        #---- build trie ---
        products.sort()
        for i in range(len(products)):
            self.insert(products[i], i)
            
        res =[]
        curr = self.prefixes
        for i in range(len(searchWord)):
            char = searchWord[i]
            if char not in curr:
                curr = {}
                res.append([])
            else:
                res.append([products[ind] for ind in curr[char]["words"]])
                curr = curr[char]

        return res