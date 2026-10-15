class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]
        while left < right:
            if max_left <= max_right:
                left += 1
                max_left = max(max_left, height[left])
                res += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                res += max_right - height[right]
        return res

        res = 0
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        while l < r:
            if maxL <= maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        return res