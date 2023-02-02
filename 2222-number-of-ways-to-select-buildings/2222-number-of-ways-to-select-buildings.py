class Solution:
    def numberOfWays(self, s: str) -> int:
        table = Counter(s[1:])
        back = {'0':0,'1':0}
        back[s[0]] += 1
        total = 0
        for x in s[1:]:
            table[x] -= 1
            if x == '0':
                total += back['1'] * table['1']
            else:
                total += back['0'] * table['0']
            back[x] += 1
        return total
