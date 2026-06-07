class Solution:
    def isPalindrome(self, s: str) -> bool:
        pointerS, pointerE = 0, len(s) - 1
        while (pointerS < pointerE):
            while (pointerS < pointerE and not s[pointerS].isalnum()):
                pointerS += 1
            while (pointerS < pointerE and not s[pointerE].isalnum()):
                pointerE -= 1
            if (s[pointerS].lower() != s[pointerE].lower()):
                return False
            pointerS += 1
            pointerE -= 1
        return True