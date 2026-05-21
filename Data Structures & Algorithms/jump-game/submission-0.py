class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0
        
        for i in range(n):
            # If we can't reach current position
            if i > max_reach:
                return False
            
            # Update the farthest we can reach
            max_reach = max(max_reach, i + nums[i])
            
            # If we can already reach or cross the last index
            if max_reach >= n - 1:
                return True
        
        return False