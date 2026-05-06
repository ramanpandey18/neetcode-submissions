class Solution:
    def search(self, nums: List[int], target: int) -> int:
        arrLen = len(nums)
        if arrLen == 1 and nums[0] == target:
            return 0
        start = 0
        end = arrLen - 1
        while start <= end:
            mid = (start + end)//2
            print("mid:", mid)
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
            print("start:", start)
            print("end:", end)
            print("updatedmid:", mid)
        return -1