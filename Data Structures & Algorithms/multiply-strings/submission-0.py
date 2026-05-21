class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Result array to store multiplication result
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        # Multiply each digit of num1 with each digit of num2
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                digit1 = int(num1[i])
                digit2 = int(num2[j])
                
                # Multiply current digits
                product = digit1 * digit2
                
                # Position in result array
                pos1 = i + j
                pos2 = i + j + 1
                
                # Add to result with carry
                total = product + result[pos2]
                result[pos2] = total % 10          # store current digit
                result[pos1] += total // 10        # carry to next position
        
        # Convert result array to string and remove leading zeros
        result_str = ''.join(map(str, result)).lstrip('0')
        
        return result_str if result_str else "0"