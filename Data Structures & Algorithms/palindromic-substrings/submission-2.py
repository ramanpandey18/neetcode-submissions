class Solution:
    def countSubstrings(self, s: str) -> int:
        # n = len(s)
        # count = 0

        # for i in range(n):
        #     # odd length palindromes
        #     left = i
        #     right = i 
        #     while(left >= 0 and right < n and s[left] == s[right]):
        #         count += 1
        #         left -= 1
        #         right += 1

        #     # even length palindromes
        #     left = i
        #     right = i + 1
        #     while(left >= 0 and right < n and s[left] == s[right]):
        #         count += 1
        #         left -= 1
        #         right += 1

        # return count   

        if not s:
            return 0
        def expand(s, l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
            
        result = 0
        for i in range(len(s)):
            result += expand(s, i, i)
            result += expand(s, i, i + 1)
        return result
    