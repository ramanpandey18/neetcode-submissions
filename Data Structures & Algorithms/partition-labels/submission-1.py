class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for k, v in enumerate(s):
            last_index[v] = k
        
        res = []
        size = end = 0
        for k, v in enumerate(s):
            size += 1
            end = max(end, last_index[v])
            if k == end:
                res.append(size)
                size = 0
        return res