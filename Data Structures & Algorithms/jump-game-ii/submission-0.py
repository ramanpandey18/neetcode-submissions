class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(n - 1):          # No need to check the last index
            # Update the farthest we can reach
            farthest = max(farthest, i + nums[i])
            
            # When we reach the end of current jump range
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # If we can already reach the end
                if current_end >= n - 1:
                    break
        
        return jumps