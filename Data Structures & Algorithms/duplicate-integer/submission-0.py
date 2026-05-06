class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arrLen = len(nums)
        if arrLen <= 1:
            return False
        dict = {}
        for i in range (0, arrLen):
            if nums[i] in dict:
                return True
            dict[nums[i]] = nums[i]
        return False
    