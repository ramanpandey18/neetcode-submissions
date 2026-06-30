class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low < high:
            mid = (low + high) // 2
            hours = sum(math.ceil(pile / mid) for pile in piles)
            if hours <= h:
                high = mid
            else:
                low = mid + 1
        return low
        
        low = 1
        high = max(piles)
        while low < high:
            mid = (low + high) // 2
            hours = sum(math.ceil(pile / mid) for pile in piles)
            if hours <= h:
                high = mid
            else:
                low = mid + 1
        return low

        lo, hi = 1, max(piles)

        while lo < hi:          # lo < hi because we want exact boundary
            mid = (lo + hi) // 2
            hours = sum(math.ceil(pile / mid) for pile in piles)

            if hours <= h:
                hi = mid        # mid works, but try slower (lower k)
            else:
                lo = mid + 1    # mid too slow, need faster

        return lo