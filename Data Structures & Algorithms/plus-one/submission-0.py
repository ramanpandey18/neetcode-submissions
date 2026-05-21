class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
    
        # Start from the last digit
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        # If we reach here, it means all digits were 9
        # Example: [9,9,9] -> [1,0,0,0]
        return [1] + digits
        