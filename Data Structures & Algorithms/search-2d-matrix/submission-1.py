class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m * n - 1

        while low <= high:
            mid = (low + high) // 2
            val = matrix[mid // n][mid % n]
            if val == target:
                return True
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            val = matrix[mid // n][mid % n]   # key conversion

            if val == target:
                return True
            elif val < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False