class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen: dict[str, int] = {}
        left = right = 0
        res = 0
        for right, ch in enumerate(s):
            if ch in last_seen:
                left = max(left, last_seen[ch] + 1)
            last_seen[ch] = right
            res = max(res, right - left + 1)
        return res
