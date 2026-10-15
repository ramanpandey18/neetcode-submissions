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
        
        n = len(nums)
        nums.sort()
        res = []
        for i, v in enumerate(nums):
            if i > 0 and v == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                sum = v + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res

        