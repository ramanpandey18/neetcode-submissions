class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2

            if nums[mid] > nums[hi]:
                lo = mid + 1    # min is in right half
            else:
                hi = mid        # min is in left half (mid included)

        return nums[lo]