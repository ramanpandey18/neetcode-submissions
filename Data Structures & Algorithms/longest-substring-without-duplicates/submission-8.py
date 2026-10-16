class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen: dict[str, int] = {}
        left = res = 0
        for idx, char in enumerate(s):
            if char in last_seen:
                left = max(left, last_seen[char] + 1)
            last_seen[char] = idx
            res = max(res, idx - left + 1)
        return res
# Iterate through each character using right as the current index.
# If the character was seen, move left to max(left, last_seen[ch] + 1).
# Update the character's latest index in last_seen.
# Update res with the maximum window length: right - left + 1.