class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ref = {chr(idx) : 0 for idx in range(ord('a'), ord('z') + 1)}
        for ch in s1:
            ref[ch] += 1
        win = {chr(idx) : 0 for idx in range(ord('a'), ord('z') + 1)}
        l = 0
        r = 0
        while r < len(s2):
            win_len = r - l + 1
            win[s2[r]] += 1
            if win_len < len(s1):
                r += 1
                continue
            if win == ref:
                return True
            else:
                win[s2[l]] -= 1
                l += 1
            r += 1
        return False



        ref = {chr(idx):0 for idx in range(ord('a') , ord('z') + 1)}
        for ch in s1:
            ref[ch] += 1
        window = {chr(idx) :0 for idx in range(ord('a'), ord('z') + 1)}
        l = 0
        r = 0
        while r < len(s2):
            window_length = r - l + 1
            window[s2[r]] += 1
            if window_length < len(s1):
                r += 1
                continue
            if window == ref:
                return True
            else:
                window[s2[l]] -= 1
                l += 1
            r += 1
        return False
    
# Build ref: count of each letter in s1 (the target permutation).
# Create an empty window counter for letters a-z.
# Move right (r) through s2, adding s2[r] to window.
# If window is smaller than len(s1), just expand: r += 1 and continue.
# If window == ref, the window is a permutation of s1, so return True.
# Otherwise, shrink from the left: window[s2[l]] -= 1, then l += 1.
# Increment r and repeat; if the loop ends, return False.
