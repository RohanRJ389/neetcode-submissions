from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap=defaultdict(list)
        tup_freq=tuple()
        for string in strs:
            
                freq_array=[0]*26
                for char in string:
                    idx=ord(char)-ord('a')
                    freq_array[idx]+=1
                hashmap[tuple(freq_array)].append(string)
        return list(hashmap.values())
            

      
        


        

        