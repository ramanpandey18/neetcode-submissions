class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        window = {}
        have, want = 0, len(need)   # unique chars satisfied vs needed
        res = ""
        resLen = float("infinity")
        l = 0

        for r in range(len(s)):
            # expand window
            c = s[r]
            window[c] = window.get(c, 0) + 1

            # check if current char satisfies a need
            if c in need and window[c] == need[c]:
                have += 1

            # shrink from left when all needs are met
            while have == want:
                # update result if this window is smaller
                if (r - l + 1) < resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1

                # remove leftmost char and shrink
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1

        return res