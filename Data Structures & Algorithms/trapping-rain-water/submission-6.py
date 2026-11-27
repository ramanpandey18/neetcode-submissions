class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]
        res = 0
        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                res += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                res += max_right - height[right]
        return res


# Why compare max_left and max_right?
# This is the key idea!

# Water at any position is:
# \[
# Water = \min(maxLeft,maxRight) - height[i]
# \]

# - If max_left < max_right, the left side determines the water level. So we can safely calculate water on the left.
# - Otherwise, the right side determines the water level. So we calculate water on the right.
# Complexity
# - Time: \(O(n)\) – Each pointer moves through the array once.
# - Space: \(O(1)\) – Only a few variables are used.
# Interview takeaway: Always process the side with the smaller maximum height because that side determines the water level.