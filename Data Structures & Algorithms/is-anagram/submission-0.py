class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for n in range(len(s)):
            if s[n] in freq:
                freq[s[n]] += 1
            else:
                freq[s[n]] = 1

        for n in range(len(t)):
            if t[n] not in freq:
                return False
            else:
                freq[t[n]] -= 1
            
        for value in freq.values():
            if value != 0:
                return False
            
        return True
