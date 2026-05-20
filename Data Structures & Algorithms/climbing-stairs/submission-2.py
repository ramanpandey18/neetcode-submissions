class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 0:
        #     return 1
        # if n < 0 :
        #     return 0

        # return self.climbStairs( n - 1) +  self.climbStairs( n - 2) 
        
        memo = {}
        
        def helper(steps_left: int) -> int:
            # 1. Base cases
            if steps_left == 0:
                return 1
            if steps_left < 0:
                return 0
            
            # 2. Check memory: If we already calculated this step, return it immediately
            if steps_left in memo:
                return memo[steps_left]
            
            # 3. Otherwise, calculate it and store the result in our memo dictionary
            memo[steps_left] = helper(steps_left - 1) + helper(steps_left - 2)
            
            return memo[steps_left]
            
        return helper(n)