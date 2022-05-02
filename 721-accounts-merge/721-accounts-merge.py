class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            r1 = find(x)
            r2 = find(y)

            if r1 != r2:
                parents[r2] = r1
        parents = {}
        emailToName = {}

        for acct in accounts:
            name = acct[0]
            for email in acct[1:]:
                emailToName[email] = name
                parents[email] = email

        for acct in accounts:
            emailA = acct[1]
            for emailB in acct[2:]:
                union(emailA, emailB)

        groups = defaultdict(list)

        for email in parents:
            r = find(email)
            groups[r].append(email)

        ans = []
        for email in groups:
            ans.append([emailToName[email]] + sorted(groups[email]))
        return ans