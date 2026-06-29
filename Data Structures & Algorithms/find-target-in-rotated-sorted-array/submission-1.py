class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


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