class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        arrLen = len(nums)
        def backtrack(i, subset):
            if i == arrLen:
                res.append(subset.copy())
                return
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            while i + 1 < arrLen and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)
        backtrack(0, [])
        return res