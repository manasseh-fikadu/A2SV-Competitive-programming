class Solution:
    def robotWithString(self, s: str) -> str:
        count, t, ans = Counter(s), [], []
        for char in s:
            t.append(char)
            if count[char] == 1:
                del count[char]
            else:
                count[char] -= 1
            while count and t and min(count) >= t[-1]:
                ans += t.pop()
        ans += t[::-1]
        return ''.join(ans)
