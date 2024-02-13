class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        elif s == "":
            return 0
        elif len(s) == 2:
            if s[0] != s[1]:
                return 2
            else:
                return 1
        
        i = 0
        max_res = 1

        while i < len(s) - 1:
            sub = s[i]
            res = 1
            j = i + 1
            while j < len(s):
                if s[j] not in sub:
                    sub = sub + s[j]
                    res += 1
                    j += 1
                else:
                    break
            max_res = max(res, max_res)
            i += 1
        
        return max_res