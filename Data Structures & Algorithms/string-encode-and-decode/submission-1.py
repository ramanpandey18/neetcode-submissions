class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            segment = str(len(s)) + "#" + s
            encodedStr += segment
        return encodedStr
    
    def decode(self, s: str) -> List[str]:
        strLen = len(s)
        i = 0
        res = []
        while i < strLen:
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
