class Solution {
public:
    bool isPalindrome(string s) {
        if (s == "") {
            return false;
        }
        int l = 0;
        int r = s.length() - 1;
        while (l < r) {
            while (l < r && !isAlnum(s[l])) {
                l++;
            }
            while (l < r && !isAlnum(s[r])) {
                r--;
            }
            if (tolower(s[l]) != tolower(s[r])) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
    bool isAlnum(char c) {
        return (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9');
    }
};
