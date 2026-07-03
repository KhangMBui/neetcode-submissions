class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # ["dag", "disk", "dog"]
        # 
        if not words or not order:
            return False
        
        char_map = {}
        for i, word in enumerate(order):
            char_map[word] = i

        def compare(word):
            res = []
            for c in word:
                res.append(char_map[c])
            return res
        
        return words == sorted(words, key=compare)
