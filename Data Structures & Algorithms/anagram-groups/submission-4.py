class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort()
        visited = {}
        
        def _get_idx(strng: str) -> Dict[str, int]:

            ref = [0]*26

            for ch in strng:
                idx = ord(ch)-ord('a')
                ref[idx] += 1
            
            return tuple(ref)
        
        for s in strs:
            idx = _get_idx(s)
            if idx not in visited:
                visited[idx] = []
            visited[idx].append(s)
        
        return list(visited.values())
    


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
 
#         strs.sort()
#         visited = {}
 
#         def _get_idx(strng: str) -> Dict[str, int]:
 
#             ref = [0]*26
 
#             for ch in strng:
#                 idx = ord(ch)-ord('a')
#                 ref[idx] += 1
 
#             return tuple(ref)
 
#         for s in strs:
#             idx = _get_idx(s)
#             if idx not in visited:
#                 visited[idx] = []
#             visited[idx].append(s)
 
#         return list(visited.values())