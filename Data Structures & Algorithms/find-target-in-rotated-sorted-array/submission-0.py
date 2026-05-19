class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid

            if nums[lo] <= nums[mid]:       # left half is sorted
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1           # target in left half
                else:
                    lo = mid + 1           # target in right half
            else:                          # right half is sorted
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1           # target in right half
                else:
                    hi = mid - 1           # target in left half

        return -1