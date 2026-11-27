class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        res = 0
        left = 0
        for right, val in enumerate(s):
            if val in last_seen:
                left = max(left, last_seen[val] + 1)
            last_seen[val] = right
            res = max(res, right - left + 1)
        return res

# Iterate through each character using right as the current index.
# If the character was seen, move left to max(left, last_seen[ch] + 1).
# Update the character's latest index in last_seen.
# Update res with the maximum window length: right - left + 1.