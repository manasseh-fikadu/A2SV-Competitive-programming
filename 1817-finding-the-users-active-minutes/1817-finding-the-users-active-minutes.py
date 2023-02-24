class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        uam = defaultdict(set)
        for log in logs:
            user, time = log[0], log[1]
            uam[user].add(time)
        count = [0] * k  
        for user in uam:
            uam_count = len(uam[user])
            if uam_count <= k:
                count[uam_count - 1] += 1
        return count
        