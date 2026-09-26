class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        arr_len = len(nums)
        
        def backtrack(i, subset):
            if i == arr_len:
                res.append(subset.copy())
                return
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            backtrack(i + 1, subset)
        backtrack(0, [])
        return res
        