class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # This is almost like...a linked list problem I've done before
        # if not word1 and not word2:
        #     return ""
        # if not word1:
        #     return word2
        # if not word2:
        #     return word1
        if not word1 and not word2:
            return ""
        first_word1 = word1[0] if word1 else ""
        first_word2 = word2[0] if word2 else ""
        print(first_word1)
        print(first_word2)
        return (
            first_word1 + first_word2 + self.mergeAlternately(word1[1:], word2[1:])
        )