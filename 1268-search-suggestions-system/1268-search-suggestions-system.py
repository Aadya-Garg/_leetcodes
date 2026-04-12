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
        l = 0
        r = len(products) - 1
        res = []
        char = ""
        for i in range(len(searchWord)):
            char += searchWord[i]
            while l <= r:
                if products[l].startswith(char):
                    break
                l += 1
            while l <= r:
                if products[r].startswith(char):
                    break
                r -= 1
            
            res.append(products[l:min(l+3, r + 1)]) if l <= r else res.append([])
        return res
        # --- now l points to the word that is >= m 
        # r points to a word that is <= m    
        # for i in range(len(products)):
        #     self.insert(products[i], i)
            
        # res =[]
        # curr = self.prefixes
        # for i in range(len(searchWord)):
        #     char = searchWord[i]
        #     if char not in curr:
        #         curr = {}
        #         res.append([])
        #     else:
        #         res.append([products[ind] for ind in curr[char]["words"]])
        #         curr = curr[char]

        return res