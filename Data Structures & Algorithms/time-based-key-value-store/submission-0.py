class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        pairs = self.store[key]
        lo, hi = 0, len(pairs) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if pairs[mid][0] <= timestamp:
                lo = mid + 1   # valid, but look for larger ts
            else:
                hi = mid - 1   # too big

        return pairs[hi][1] if hi >= 0 else ""
