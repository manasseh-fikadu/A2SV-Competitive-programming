class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def helper(combination, start, remaining_slots):
            if remaining_slots == 0:
                ans.append(combination)
            else:
                for num in range(start, n + 1):
                    helper(combination + [num], num + 1, remaining_slots - 1)
        
        ans = []
        helper([], 1, k)

        return ans