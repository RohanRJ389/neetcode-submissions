class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        hashmap = {} # number: its index

        for idx,n in enumerate(numbers):
            
            if n in hashmap.keys():
                return [hashmap[n]+1, idx+1]

            diff = target - n

            hashmap[diff] = idx

        return []
