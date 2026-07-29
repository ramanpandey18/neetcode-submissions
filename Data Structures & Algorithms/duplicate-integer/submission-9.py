class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

        # seen = {}
        # for i, num, in enumerate(nums):
        #     if num in seen:
        #         return True
        #     seen[num] = i
        # return False