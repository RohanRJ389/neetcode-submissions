from collections import Counter

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map={}

        for idx,val in enumerate(nums):
            diff = target-val
            if diff in diff_map:
                return[diff_map[diff],idx]
            diff_map[val]=idx
        return []