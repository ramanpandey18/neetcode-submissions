class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for idx, val in enumerate(nums):
            if idx > 0 and val == nums[idx - 1]:
                continue
            left = idx + 1
            right = n - 1
            while left < right:
                curr_sum = val + nums[left] + nums[right]
                if curr_sum == 0:
                    res.append([val, nums[left], nums[right]])
                    left += 1
                    while (left<right and nums[left]==nums[left - 1]):
                        left += 1
                elif curr_sum > 0:
                    right -= 1
                else:
                    left += 1
        return res
