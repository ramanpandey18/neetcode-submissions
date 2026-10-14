class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # dp[sum] = number of ways to reach this sum
        dp = {0: 1}

        # Process each number one by one
        for num in nums:

            # Store the new sums after using this number.
            new_dp = {}

            # Try adding and subtracting the current number
            # from every sum we have created so far.
            for current_sum, ways in dp.items():

                # Option 1: Add the current number
                add_sum = current_sum + num
                new_dp[add_sum] = new_dp.get(add_sum, 0) + ways

                # Option 2: Subtract the current number
                subtract_sum = current_sum - num
                new_dp[subtract_sum] = new_dp.get(subtract_sum, 0) + ways

            # Move to the next number
            dp = new_dp

        # Number of ways to reach the target
        return dp.get(target, 0)
