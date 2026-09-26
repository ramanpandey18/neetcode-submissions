class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        arr_len = len(nums)

        def backtrack(i, subset):
            if i == arr_len:
                res.append(subset.copy())
                return
            
            subset.append(nums[i])

            backtrack(i + 1, subset)
            
            subset.pop() 

            while i + 1 < arr_len and nums[i] == nums[i + 1]:
                i += 1

            backtrack(i + 1, subset)

        backtrack(0, [])

        return res       