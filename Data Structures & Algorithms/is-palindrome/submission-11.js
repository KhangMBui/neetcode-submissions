class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        if (s == "") {
            return false;
        }
        let l = 0;
        let r = s.length - 1;
        while (l < r) {
            while (l < r && !this.alphaNum(s[l])) {
                l += 1;
            }
            while (l < r && !this.alphaNum(s[r])) {
                r -= 1;
            }
            if (s[l].toLowerCase() != s[r].toLowerCase()) {
                return false;
            }
            l += 1;
            r -= 1
        }
        return true
    }

    alphaNum(c) {
        return (c >= 'A' && c <= 'Z' || c >= 'a' && c <= 'z' || c >= '0' && c <= '9');
    }
}
