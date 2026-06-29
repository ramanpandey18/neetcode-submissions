class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        i = 0
        j = 0
        median1 = 0
        median2 = 0
        
        for count in range((len1 + len2) // 2 + 1):
            median2 = median1
            if i < len1 and j < len2:
                if nums1[i] > nums2[j]:
                    median1 = nums2[j]
                    j += 1
                else:
                    median1 = nums1[i]
                    i += 1
            elif i < len1:
                median1 = nums1[i]
                i += 1
            else:
                median1 = nums2[j]
                j += 1
            if (len1 + len2) % 2 == 1:
                return float(median1)
            else:
                return (median1 + median2) / 2.0


        len1, len2 = len(nums1), len(nums2)
        i = j = 0
        median1 = median2 = 0

        for count in range((len1 + len2) // 2 + 1):
            median2 = median1
            if i < len1 and j < len2:
                if nums1[i] > nums2[j]:
                    median1 = nums2[j]
                    j += 1
                else:
                    median1 = nums1[i]
                    i += 1
            elif i < len1:
                median1 = nums1[i]
                i += 1
            else:
                median1 = nums2[j]
                j += 1

        if (len1 + len2) % 2 == 1:
            return float(median1)
        else:
            return (median1 + median2) / 2.0
            
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half = (m + n) // 2

        lo, hi = 0, m  # i can range from 0..m (cut positions in nums1)

        while True:
            i = (lo + hi) // 2   # cut in nums1: i elements go to left
            j = half - i          # cut in nums2: j elements go to left

            # Edge values around the cut (use -inf/+inf for boundaries)
            nums1_left  = nums1[i - 1] if i > 0 else float('-inf')
            nums1_right = nums1[i]     if i < m else float('inf')
            nums2_left  = nums2[j - 1] if j > 0 else float('-inf')
            nums2_right = nums2[j]     if j < n else float('inf')

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # ✅ Valid partition found
                max_left  = max(nums1_left, nums2_left)
                min_right = min(nums1_right, nums2_right)

                if (m + n) % 2 == 1:
                    return float(min_right)       # odd total: median is min of right
                else:
                    return (max_left + min_right) / 2.0   # even total: average

            elif nums1_left > nums2_right:
                hi = i - 1   # i is too large, move left
            else:
                lo = i + 1   # i is too small, move right
