class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if not words or not order:
            return False
            
        order_index = {c: i for i, c in enumerate(order)}

        def in_order(word1, word2):
            # Compare character by character
            for i in range(min(len(word1), len(word2))):
                c1, c2 = word1[i], word2[i]

                # First different character decides the order
                if c1 != c2:
                    return order_index[c1] < order_index[c2]

            # If all compared chars are the same,
            # shorter/equal word must come first
            return len(word1) <= len(word2)

        for i in range(len(words) - 1):
            if not in_order(words[i], words[i + 1]):
                return False

        return True