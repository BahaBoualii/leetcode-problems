class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1

        if len(nums) == 1 and nums[0] == target:
            return 0

        while i <= j:
            mid = (j + i) // 2
            if target > nums[mid]:
                i = mid + 1
            elif target < nums[mid]:
                j = mid - 1
            else:
                return mid
        return -1