class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        merged = [0, 0, 0]

        for a, b, c in triplets:
            if a > x or b > y or c > z:
                continue
            merged[0] = max(merged[0], a)
            merged[1] = max(merged[1], b)
            merged[2] = max(merged[2], c)
        return merged == list(target)

        
        
        
        
        
        
        
        x, y, z = target
        merged = [0, 0, 0]

        for a, b, c in triplets:
            # Skip any triplet that would overshoot the target in any position.
            # Merging it could permanently raise a value beyond what target needs.
            if a > x or b > y or c > z:
                continue

            # This triplet is safe — absorb its maximums
            merged[0] = max(merged[0], a)
            merged[1] = max(merged[1], b)
            merged[2] = max(merged[2], c)

        return merged == list(target)