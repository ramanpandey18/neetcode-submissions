class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        visited = [False] * n
        def backtrack(current):
            if len(current) == n:
                res.append(list(current))
                return
            for i in range(n):
                if visited[i]:
                    continue
                visited[i] = True
                current.append(nums[i])
                backtrack(current)
                visited[i] = False
                current.pop()
        backtrack([])
        return res
        