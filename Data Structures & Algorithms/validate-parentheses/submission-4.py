class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')' : '(', '}' : '{', ']' : '['}
        stack = []
        for char in s:
            if char not in mapping:
                stack.append(char)
            else:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        if not stack:
            return True
        return False

        mapping = {')' : '(', '}' : '{', ']': '['}
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != mapping[char]:
                    return False
        if not stack:
            return True
        return False 
