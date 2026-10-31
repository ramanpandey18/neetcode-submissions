class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top = 0
        bottom = len(matrix) - 1
        left = 0 
        right = len(matrix[0]) - 1
        # Left → Right (Top row)
        while top <= bottom and left <= right:
            for j in range (left, right + 1):
                res.append(matrix[top][j])
            top += 1

            # Top → Bottom (Right column)
            for i in range(top, bottom  + 1):
                res.append(matrix[i][right])
            right -= 1
            # Right → Left (Bottom row)
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1
            # Bottom → Top (Left column)
            if left <= right:
                for i in range(bottom, top - 1,  -1):
                    res.append(matrix[i][left])
                left += 1
        return res

 
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            for j in range(left, right + 1):        # left → right
                res.append(matrix[top][j])
            top += 1
            for i in range(top, bottom + 1):        # top → bottom
                res.append(matrix[i][right])
            right -= 1
            if top <= bottom:          # bottom row (right → left)
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1
            if left <= right:  # left column (bottom → top)
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res

        
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        result = []
        # rows = len(matrix)
        # cols = len(matrix[0])
        while top <= bottom and left <= right:
            # 1. Traverse RIGHT across the top row
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            
            # 2. Traverse DOWN along the right column
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            
            # 3. Traverse LEFT across the bottom row (if still valid)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            
            # 4. Traverse UP along the left column (if still valid)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
    
        return result
        