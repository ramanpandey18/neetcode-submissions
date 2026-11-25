class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        arr_len = len(nums)
        def backtrack(start, current, remaining):
            if remaining == 0:
                res.append(current.copy())
                return
            
            if remaining < 0:
                return
            
            for i in range(start, arr_len):
                current.append(nums[i])
                backtrack(i, current, remaining - nums[i])
                current.pop()
        backtrack(0, [], target)
        return res
