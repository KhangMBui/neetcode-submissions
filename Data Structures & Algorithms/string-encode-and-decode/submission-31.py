class Solution:
    # Understanding the problem:
    # ["neet", "code", "love", "you"] -> encode into a string
    # that string -> decode back to the array
    # Decode is fairly easy as we can just loop through the array and
    # get the string
    # but how would we decode it back
    # wouldn't we need some thing to spot where the word starts and ends?
    # => we can put in the size of the word, e.g. neet => 4neet
    # However, when we traverse through the encoded string, what if there's
    # word that has a number in it? That would lead to the word getting mixup.
    # So we need like a special character to detect where word starts and ends
    # while the number helps us identify how long that word is
    # => 4$neet4$code4$love3$you, whenever reached $, we get the 
    # number and then find the word with that length, adding back to 
    # the array
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        encodeStr = ""
        for s in strs:
            encodeStr += str(len(s)) + "$" + s
        return encodeStr
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        decodedStrs = []
        r = 0
        # Use a sliding window/two pointers to iterate
        while r < len(s):
            l = r
            while (s[r] != "$"):
                r += 1
            length = int(s[l:r])
            decodedStrs.append(s[r + 1: r + 1 + length])
            r += 1 + length
        return decodedStrs