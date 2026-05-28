class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        n = len(s)

        def is_palindrome(sub):
            return sub == sub[::-1] 

        def backtrack(start, current):
            if start == n:
                result.append(list(current))
                return
            for end in range(start + 1, n + 1):
                substring = s[start:end]   
                if is_palindrome(substring):
                    current.append(substring)
                    backtrack(end, current)
                    current.pop()
        backtrack(0, [])
        return result    