class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        mapping = {}
        for i in range(n):
            if (target - nums[i]) in mapping:
                return [mapping[target - nums[i]], i]
            mapping[nums[i]] = i
