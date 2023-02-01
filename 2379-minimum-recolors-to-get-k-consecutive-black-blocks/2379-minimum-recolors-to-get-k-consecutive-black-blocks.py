class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        wcount, count = 0, 0
        for i in range(k):
            if blocks[i] == 'W': 
                wcount += 1

        count = wcount
        j = 0
        for i in range(k, len(blocks)):
            if blocks[j] == 'W':
                wcount -= 1
            j += 1
            if blocks[i] == 'W':
                wcount += 1
            count = min(count, wcount)

        return count
        