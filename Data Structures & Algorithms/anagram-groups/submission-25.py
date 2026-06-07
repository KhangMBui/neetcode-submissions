class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Question, group anagrams into different lists inside a list
        # We can use hashmap to find anagram
        if not strs:
            return []
        
        # This hashmap stores (key: hashmap of character freq, value: list of anagrams)
        anagram_hashmap = defaultdict(list)

        for s in strs:
            char_freq = [0]*26
            for c in s:
                char_freq[ord(c) - ord('a')] += 1
            anagram_hashmap[tuple(char_freq)].append(s)
        
        return anagram_hashmap.values()
            