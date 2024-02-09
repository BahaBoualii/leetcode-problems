class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            k = (right+left) // 2
            hours = 0

            for i in piles:
                hours += math.ceil(i / k)
            
            if hours > h:
                left = k + 1
            elif hours <= h:
                res = min(k ,res)
                right = k - 1
        
        return res

            