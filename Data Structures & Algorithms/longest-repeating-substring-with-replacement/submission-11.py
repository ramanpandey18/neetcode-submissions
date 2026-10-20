from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq: dict[str, int] = defaultdict(int)
        left = max_freq = res = 0
        for idx, char in enumerate(s):
            freq[char] += 1
            max_freq = max(max_freq, freq[char])
            while (idx - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left +=1
            res = max(idx - left + 1, res)
        return res 


        freq: dict[str, int] = defaultdict(int)
        left = max_freq = best = 0
        for right, ch in enumerate(s):
            freq[ch] += 1
            max_freq = max(max_freq, freq[ch])
            # more than k chars would need replacing -> shrink window
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            best = max(best, right- left + 1)
        return best

# Initialize freq, left = 0, max_freq = 0, and best = 0.
# Iterate through each character using right as the current index.
# Increment the frequency of the current character in freq.
# Update max_freq with the highest character frequency seen so far.
# While (window length - max_freq) > k, decrease the frequency of s[left] and increment left.
# Update best with the maximum valid window length: right - left + 1.