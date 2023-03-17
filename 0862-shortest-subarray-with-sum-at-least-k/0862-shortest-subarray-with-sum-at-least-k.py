class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        N = len(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        # Want smallest y-x with Py - Px >= K
        ans = N+1 # N+1 is impossible
        monoq = collections.deque() 
        for y, Py in enumerate(P):
            while monoq and Py <= P[monoq[-1]]:
                monoq.pop()

            while monoq and Py - P[monoq[0]] >= K:
                ans = min(ans, y - monoq.popleft())

            monoq.append(y)

        return ans if ans < N+1 else -1