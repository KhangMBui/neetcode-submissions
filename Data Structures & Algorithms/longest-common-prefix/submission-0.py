class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Use the first string as a starting prefix
        # then compare it against every other string

        # For each word in strs:
        # while word does not start with prefix:
        #   shorten prefix by 1 character from the end
        # Eventually, either prefix is empty, or every word starts with it

        if not strs:
            return ""
        
        prefix = strs[0]

        for s in strs:
            while not s.startswith(prefix):
                prefix = prefix[:len(prefix) - 1]
        
        return prefix