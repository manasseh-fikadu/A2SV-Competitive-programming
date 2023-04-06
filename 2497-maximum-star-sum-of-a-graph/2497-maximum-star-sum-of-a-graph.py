import queue

class Solution:
    def maxStarSum(self, vals: List[int], fs: List[List[int]], k: int) -> int:
        n = len(vals)
        edges = [queue.PriorityQueue() for i in range(n)]

        # Fill up data structures
        for i in range(len(fs)):
            f = fs[i][0]
            s = fs[i][1]
            edges[f].put((-vals[s], s))
            edges[s].put((-vals[f], f))

        ans = float('-inf')
        for i in range(n):
            prev = vals[i]
            current = vals[i]
            num = k

            # Getting answer from each priority queue
            while num > 0 and not edges[i].empty():
                prev = current
                val, idx = edges[i].get()
                current += -val

                if current < prev:
                    current = prev
                    break

                num -= 1

            ans = max(ans, current)

        return ans
