class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        l, r = 0, len(height) - 1
        while l < r:
            contained_water = (r - l) * min(height[l], height[r])
            max_water = max(contained_water, max_water)
            
            if height[l] < height[r]:
                l += 1
            elif height[r] < height[l]: 
                r -= 1
            else:
                l += 1

        return max_water
