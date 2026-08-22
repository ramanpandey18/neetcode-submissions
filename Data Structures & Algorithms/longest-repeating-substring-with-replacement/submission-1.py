class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_f = 0
        res = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            max_f = max(max_f, count[s[r]])

            while (r - l + 1) - max_f > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res 

        # count = {}
        # l = 0
        # res = 0
        # maxf = 0
        # n = len(s)
        
        # for r in range(n):
        #     count[s[r]] = count.get(s[r], 0) + 1
            
        #     maxf = max(maxf, count[s[r]])
            
        #     while (r-l+1) - maxf > k:
        #         count[s[l]] -= 1
        #         l += 1
            
        #     res = max(res, r - l + 1)
        
        # return res
