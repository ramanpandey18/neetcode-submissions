class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for char in strs:
            segment = str(len(char)) + "#" + char
            encoded_str += segment
        return encoded_str

    def decode(self, s: str) -> List[str]:
        n = len(s)
        res = []
        i = 0
        while i < n:
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i: j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res
