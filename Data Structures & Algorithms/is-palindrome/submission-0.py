class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ""

        for i in s:
            if i.isalnum():
                cleaned_s += i.lower()

        for i in range(int(len(cleaned_s) / 2)):
            if cleaned_s[i] != cleaned_s[-i - 1]:
                return False

        return True
