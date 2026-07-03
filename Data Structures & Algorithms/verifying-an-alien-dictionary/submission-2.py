class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        order_index = {}
        for index, char in enumerate(order):
            order_index[char] = index
        
        def compare(words):
            res = []
            for c in words:
                res.append(order_index[c])
            return res
        
        return words == sorted(words, key=compare)