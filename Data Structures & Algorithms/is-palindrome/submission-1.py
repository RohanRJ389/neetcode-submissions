class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ""

        for i in s:
            if i.isalnum():
                cleaned_s += i.lower()

        l,r=0,len(cleaned_s)-1

        while l<r:
            if cleaned_s[l]!=cleaned_s[r]:
                return False
            r-=1
            l+=1

        return True
