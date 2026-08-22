class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ref = {chr(idx):0 for idx in range(ord('a'), ord('z') + 1)}
        for ch in s1:
            ref[ch] += 1 
        l, r = 0, 0
        window = {chr(idx):0 for idx in range(ord('a'), ord('z') + 1)}
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


        # ref = {chr(idx):0 for idx in range(ord('a'), ord('z')+1)}
        # for ch in s1:
        #     ref[ch] += 1
        # l, r = 0, 0
        # window = {chr(idx):0 for idx in range(ord('a'), ord('z')+1)}
        # while r < len(s2):
        #     window_length = r-l+1
        #     window[s2[r]] += 1
        #     if window_length < len(s1):
        #         r += 1
        #         continue
        #     if window == ref:
        #         return True
        #     else:
        #         window[s2[l]] -= 1
        #         l += 1
        #     r += 1
        
        # return False
