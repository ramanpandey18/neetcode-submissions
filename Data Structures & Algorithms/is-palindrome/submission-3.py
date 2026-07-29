class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        sLen = len(s)
        if sLen <= 1:
            return True
        left = 0
        right = sLen - 1
        while left <= right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True



        s = s.replace(" ", "")
        sLen = len(s)
        if sLen <= 1:
            return True
        p1 = 0
        p2  = sLen - 1
        while p1 <= p2:
            if not s[p1].isalnum():
                p1 += 1
                continue
            if not s[p2].isalnum():
                p2 -= 1
                continue
            if s[p1].lower() != s[p2].lower():
                return False
            p1 += 1
            p2 -= 1
        return True
            
       
        