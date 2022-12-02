class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = defaultdict(int)
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            d[domain] += count
            while '.' in domain:
                domain = domain[domain.index('.')+1:]
                d[domain] += count
        return ["{} {}".format(v, k) for k, v in d.items()]