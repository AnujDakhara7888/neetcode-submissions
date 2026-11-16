class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        map = {}
        for i in range(len(s)):
            map[s[i]] = map.get(s[i], 0) + 1

        for i in range(len(t)):
            if t[i] in map:
                map[t[i]]-=1
            else:
                return False
            if map[t[i]]<0:
                return False

        return True