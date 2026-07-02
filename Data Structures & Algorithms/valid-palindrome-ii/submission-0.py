class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Two pointers like regular problem
        # Match => Keep going
        # Mismatch => we could perhaps get rid of left or right character, 
        # and check if it results in a palindrome for the remaining substring

        l, r = 0, len(s) - 1

        # bbd
        # abbadc

        while l < r:
            if s[l] != s[r]:
                skipL = s[l + 1 : r + 1] # r + 1 exclusive
                skipR = s[l : r] # l inclusive
                # See if either version works
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            else:
                l += 1
                r -= 1
        return True
