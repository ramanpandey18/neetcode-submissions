class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        mapping = {}
        for i, val in enumerate(nums):
            if target - val in mapping:
                return [mapping[target - val], i]
            mapping[val] = i
