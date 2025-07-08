class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        set1 = set(word1)
        set2 = set(word2)
        if (set1 != set2):
            return False
            
        freq1 = {}
        freq2 = {}
        for i in set1:
            freq1[i] = word1.count(i)
            freq2[i] = word2.count(i)

        l1 = sorted(freq1.values())
        l2 = sorted(freq2.values())
        return (l1 == l2)
        