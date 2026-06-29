class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1 and target == nums[0]:
            return 0
        start = 0
        end = n - 1
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1 