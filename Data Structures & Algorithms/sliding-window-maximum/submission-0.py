class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()   # stores indices, decreasing order of values
        res = []
        l = 0

        for r in range(len(nums)):
            # remove from back: smaller elements are useless
            while dq and nums[dq[-1]] <= nums[r]:
                dq.pop()

            dq.append(r)

            # remove from front: out of window
            if dq[0] < l:
                dq.popleft()

            # window is fully formed
            if r >= k - 1:
                res.append(nums[dq[0]])
                l += 1

        return res