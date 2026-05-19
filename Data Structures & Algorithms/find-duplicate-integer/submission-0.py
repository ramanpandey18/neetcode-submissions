class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        
        # Move slow by 1 step and fast by 2 steps until they meet
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        # Phase 2: Find the entrance to the cycle (the duplicate number)
        # Reset slow to the beginning of the array
        slow = nums[0]
        
        # Move both pointers 1 step at a time until they meet again
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        # Their meeting point is the duplicate number
        return slow