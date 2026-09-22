class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s,len_t=len(s),len(t)

        if len_s!=len_t:
            return False

        count_s,count_t={},{}

        for i in range(len_s):
            count_s[s[i]]=count_s.get(s[i],0)+1
            count_t[t[i]]=count_t.get(t[i],0)+1

        if count_s!=count_t:
            return False
        return True