class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result

        result = [0] * len(temperatures)
        stack = []  # stores indices

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)

        return result

# Initialize result with all zeros and an empty stack.
# Iterate through temperatures using i (index) and temp (current temperature).
# While the stack is not empty and temp > temperatures[stack[-1]], pop the index idx.
# Calculate the waiting days: result[idx] = i - idx.
# Push the current index i onto the stack.