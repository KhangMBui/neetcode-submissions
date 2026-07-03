class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Instead of sorting, we can directly verify that
        # each word is lexicographically <= next word
        # according to alien order

        order_index = {c : i for i, c in enumerate(order)}
        print("order_index: ", order_index)
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            print("word1, word2: ", word1, word2)
            # Compare the 2 words, perhaps using 2 pointers
            ptr1 = ptr2 = 0

            while ptr1 < len(word1) and ptr2 < len(word2):
                move_on = False
                # In case the 2 letters are different:
                if word1[ptr1] != word2[ptr2]:
                    # Check letter1 is lexicographically <= than letter2
                    if order_index[word1[ptr1]] > order_index[word2[ptr2]]:
                        return False
                    else: # If <=, then we can move on
                        move_on = True
                        break
                ptr1 += 1
                ptr2 += 1

            if move_on: continue
            # Here, the 2 words are identical so far, but one word
            # may still haven't been done iterated yet. And the 
            # longer one should be word2
            if word1[:ptr1] == word2[:ptr2]:
                print("hehe")
                if len(word2) < len(word1):
                    return False
        
        return True

            