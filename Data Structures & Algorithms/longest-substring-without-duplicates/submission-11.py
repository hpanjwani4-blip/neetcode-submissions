class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        j = 0
        seen = {}
        if len(s) == 0:
            return 0
        seen[s[0]] = 0
        for i in range(1, len(s)):
            # print(i, j , seen)
            if s[i] not in seen:
                seen[s[i]] = i
                res = max(res, (i-j)+1)
                # print(res)

            else:
                if seen[s[i]] < j:
                    seen[s[i]] = i
                    res = max(res, (i-j)+1)
                else:
                    j = seen[s[i]]+1
                    seen[s[i]] = i
                    res = max(res, (i-j)+1)
                # print(res)

        return max(res, len(s)-j)
        