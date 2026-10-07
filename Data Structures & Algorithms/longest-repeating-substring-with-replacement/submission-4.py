from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq: dict[str, int] = defaultdict(int)
        left = max_freq = best = 0
        for right, ch in enumerate(s):
            freq[ch] += 1
            max_freq = max(max_freq, freq[ch])
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            best = max(best, right- left + 1)
        return best

        freq: dict[str, int] = defaultdict(int)
        left = max_freq = best = 0

        for right, ch in enumerate(s):
            freq[ch] += 1
            max_freq = max(max_freq, freq[ch])

            # more than k chars would need replacing -> shrink window
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best
