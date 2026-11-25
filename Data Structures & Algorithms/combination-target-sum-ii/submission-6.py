class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)
        def backtrack(start, current, remaining):
            if remaining == 0:
                res.append(current.copy())
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break
                current.append(candidates[i])
                backtrack(i + 1, current, remaining - candidates[i])
                current.pop()
        backtrack(0, [], target)
        return res



        candidates.sort()
        result = []
        arr_len = len(candidates)
        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(current.copy())
                return
            for i in range(start, arr_len):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break
                current.append(candidates[i])
                backtrack(i + 1, current, remaining - candidates[i])
                current.pop()
        backtrack(0, [], target)
        return result
        