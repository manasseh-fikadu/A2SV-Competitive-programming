class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d = defaultdict(list)
        S = set()
        for i, s in enumerate(senate):
            d[s].append(i)
            S.add(i)
        while True:
            for i, s in enumerate(senate):
                if not d['R']:
                    return 'Dire'
                if not d['D']:
                    return 'Radiant'
                if s == 'R':
                    if i not in S:
                        continue
                    idx = bisect_right(d['D'],i)
                    if idx == len(d['D']):
                        a = d['D'].pop(0)
                        S.remove(a)
                    else:
                        a = d['D'].pop(idx)
                        S.remove(a)
                else:
                    if i not in S:
                        continue
                    idx = bisect.bisect_right(d['R'],i)
                    if idx == len(d['R']):
                        a = d['R'].pop(0)
                        S.remove(a)
                    else:
                        a=d['R'].pop(idx)
                        S.remove(a)
            
                