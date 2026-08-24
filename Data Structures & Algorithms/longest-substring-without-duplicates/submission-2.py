class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapping : Dict[str, int] = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in mapping:
                l = max(mapping[s[r]] + 1, l)
            mapping[s[r]] = r
            res = max(res, r - l + 1)
        return res        

        