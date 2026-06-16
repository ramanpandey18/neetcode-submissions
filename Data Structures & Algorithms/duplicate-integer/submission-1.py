class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        n = len(nums)
        if n <= 1:
            return False

        hashmap = {}
        for i in range(n):
            if nums[i] in hashmap:
                return True
            hashmap[nums[i]] = i
        return False

    

        