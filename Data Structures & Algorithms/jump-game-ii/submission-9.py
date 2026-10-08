class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        count = end = max_reach = 0
        for i in range(n - 1):
            max_reach = max(max_reach, i + nums[i])
            if i == end:
                count += 1
                end = max_reach
                if max_reach >= n - 1:
                    return count
        return count
        