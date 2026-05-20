class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(list(current))
                return
            if remaining < 0:
                return

            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i, current, remaining - nums[i])  # i, not i+1 (reuse allowed)
                current.pop()           # Undo choice (backtrack)

        backtrack(0, [], target)
        return result