class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        ans = []
        stamp,target=target,stamp
        stamp = list(stamp)
        while stamp.count('?')!=len(stamp):
            for i in range(len(stamp)):
                if i + len(target)-1==len(stamp):
                    return []
                ok = 1
                word = 0
                for j in range(len(target)):
                    if stamp[i+j]==target[j] or stamp[i+j]=='?':
                        if stamp[i+j]!='?':
                            word+=1
                        continue
                    ok=0
                    break
                if ok and word:
                    ans.append(i)
                    for j in range(i,i+len(target)):
                        stamp[j]='?'
                    break 
        return reversed(ans)