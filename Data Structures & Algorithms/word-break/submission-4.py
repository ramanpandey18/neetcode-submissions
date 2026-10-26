class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#  Goal: Check if string s can be split into words that all exist in wordDict.
# 1. Start DFS from index i = 0.
# 2. If i == len(s), we have matched the entire string, so return True.
# 3. If index i is in memo, return the previously computed result.
# 4. Loop through each word in wordDict.
# 5. If s.startswith(word, i) is true, the word matches at index i. Recursively check from i + len(word).
# 6. If any recursive call returns True, store memo[i] = True and return True.
# 7. If no word leads to a valid split, store memo[i] = False and return False.
# 8. Finally, return dfs(0).
        memo = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            for word in wordDict:
                if s.startswith(word, i):
                    if dfs(i + len(word)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return dfs(0)

        memo = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            for word in wordDict:
                if s.startswith(word, i):
                    if dfs(i + len(word)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return dfs(0)
