class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        l, r = 0, n - 1
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max (res, area)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] >= heights[r]:
                r -= 1
        return res