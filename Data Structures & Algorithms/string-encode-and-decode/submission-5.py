class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            segment = str(len(s)) + "#" + s
            encoded_str += segment
        print(f"encoded_str is {encoded_str}")
        return encoded_str

    def decode(self, s: str) -> List[str]:
        n = len(s)
        res = []
        i = 0
        while i < n:
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i : j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res