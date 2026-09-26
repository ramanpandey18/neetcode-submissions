class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, current, remaining):

            # We found a valid combination.
            if remaining == 0:
                result.append(current.copy())
                return

            # The sum has gone beyond the target.
            if remaining < 0:
                return

            # Try every number starting from 'start'.
            for i in range(start, len(nums)):

                # Choose nums[i]
                current.append(nums[i])

                # We pass i, NOT i + 1.
                # This allows us to use nums[i] again.
                backtrack(
                    i,
                    current,
                    remaining - nums[i]
                )

                # Undo the choice.
                current.pop()

        backtrack(0, [], target)

        return result
        