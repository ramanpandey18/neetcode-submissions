class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def is_palindrome(subs: str) -> bool:
            return subs == subs[::-1]
        
        def backtrack(start, current):
            if start == n:
                res.append(list(current))
                return
            
            for end in range(start + 1, n + 1):
                sub = s[start:end]
                if is_palindrome(sub):
                    current.append(sub)
                    backtrack(end, current)
                    current.pop()
        backtrack(0, [])
        return res

        