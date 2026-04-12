class TrieNode:
        __slots__ = ["prefixes", "words"]
        def __init__(self):
            self.prefixes = collections.defaultdict(TrieNode)
            self.words = []

        def insert(self, word: str, index: int) -> None:
            curr = self
            for char in word: # so total = O(length of word)
                curr = curr.prefixes[char] #constant
                if len(curr.words) < 3: # constant
                    curr.words.append(index)

                
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        #---- build trie ---
        products.sort() #O(nlogn)
        # l = 0
        # r = len(products) - 1
        # res = []
        # char = ""
        # for i in range(len(searchWord)):
        #     char += searchWord[i]
        #     while l <= r:
        #         if products[l].startswith(char):
        #             break
        #         l += 1
        #     while l <= r:
        #         if products[r].startswith(char):
        #             break
        #         r -= 1
            
        #     res.append(products[l:min(l+3, r + 1)]) if l <= r else res.append([])
        # return res
        root = TrieNode()
        for i, word in enumerate(products): #O(total # of characters in products)
            root.insert(word, i)
     
        res = []
        curr = root
        for char in searchWord:
            if curr and char in curr.prefixes:
                curr = curr.prefixes[char]
                res.append([products[ind] for ind in curr.words])
                
            else:
                res.append([])
                curr = None

        return res