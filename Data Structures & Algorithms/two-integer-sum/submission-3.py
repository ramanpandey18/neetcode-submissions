class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashmap = {}

        for i in range(n):
            if (target - nums[i]) in hashmap:
                return [hashmap[target - nums[i]], i]
            hashmap[nums[i]] = i 
        