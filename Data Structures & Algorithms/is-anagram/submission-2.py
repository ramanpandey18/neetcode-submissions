class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lenS = len(s)
        lenT = len(t)
        if lenS == 0 or lenT == 0:
            return False
        if lenS != lenT:
            return False
        dictS = {}
        dictT = {}
        for i in range(0, lenS):
            if s[i] in dictS:
                dictS[s[i]] += 1
            else:
                dictS[s[i]] = 1
            if t[i] in dictT:
                dictT[t[i]] += 1
            else:
                dictT[t[i]] = 1
        
        if len(dictS) != len(dictT):
            return False
        else:
            for key in dictS:
                if key not in dictT or dictS[key] != dictT[key]:
                    return False
        return True