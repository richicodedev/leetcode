class Solution:
    def reverseVowels(self, s: str) -> str:
        from collections import deque

        vow_in_s = []
        slen = len(s)
        vow = "aeiou"

        for i in range(slen):
            if s[i].lower() in vow:
                vow_in_s.append(s[i])

        vow_in_s.reverse()
        dq = deque(vow_in_s)

        res = ""
        for i in range(slen):
            if s[i].lower() in vow:
                res += dq.popleft()
            else:
                res += s[i]
        return res