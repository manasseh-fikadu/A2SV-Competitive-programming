class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        if start == end:
            return 0
        bank = set(bank)
        queue = [start]
        visited = set()
        visited.add(start)
        level = 0
        while queue: 
            level += 1
            for _ in range(len(queue)):
                curr = queue.pop(0)
                for i in range(len(curr)):
                    for j in ['A', 'C', 'G', 'T']:
                        new = curr[:i] + j + curr[i+1:]
                        if new == end:
                            return level
                        if new in bank and new not in visited:
                            visited.add(new)
                            queue.append(new)
                            
        return -1