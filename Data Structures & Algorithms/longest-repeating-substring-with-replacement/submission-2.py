class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        max_f = 0
        count : dict[str, int] = {}
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            max_f = max(count[s[r]], max_f)

            while (r - l + 1 ) - max_f > k:
                count[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        return res
