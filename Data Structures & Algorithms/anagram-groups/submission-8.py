class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort()
        visited = {}
        def _get_idx(s: str) -> tuple[int, int]:
            ref = [0] * 26
            for ch in s:
                idx = ord(ch) - ord('a')
                ref[idx] += 1
            return tuple(ref)
        for word in strs:
            idx = _get_idx(word)
            if idx not in visited:
                visited[idx] = []
            visited[idx].append(word)
        return list(visited.values())


        
        strs.sort()
        visited = {}

        def _get_idx(s: str) -> tuple[int, int]:
            ref = [0] * 26
            for ch in s:
                idx = ord(ch) - ord('a')
                ref[idx] += 1
            return tuple(ref)        
        
        for word in strs:
            idx = _get_idx(word)
            if idx not in visited:
                visited[idx] = []
            visited[idx].append(word)
        return list(visited.values())
        
        # {
        #     key_for_ate_eat_tea: ["ate", "eat", "tea"],
        #     key_for_bat: ["bat"],
        #     key_for_nat_tan: ["nat", "tan"]
        # }