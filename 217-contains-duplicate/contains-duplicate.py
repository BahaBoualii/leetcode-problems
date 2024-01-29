class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicates_map = {}
        for i in nums:
            if i in duplicates_map:
                return True
            else:
                duplicates_map[i] = 1
        return False