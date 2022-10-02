class Solution:
    def numRollsToTarget(self, d: int, k: int, target: int) -> int:
        '''
        def helper(h, d, target):
            # if target is too small or if it is out of range
            if target <= 0 or target > (d * f):
                return 0
            if d == 1:
                return 1        # no need to check if target is within reach; already done before
            if (d, target) in h:
                return h[(d, target)]        # directly access from hash table
            res = 0
            for i in range(1, f + 1):
                res += helper(h, d - 1, target - i)       # check all possible combinations
            h[(d, target)] = res
            return h[(d, target)]

        h = {}
        return helper(h, d, target) % (10 ** 9 + 7)
        '''
        def dp(h, d, target):
            if target <= 0 or target > (d * k):
                return 0
            if d == 1:
                return 1
            if (d, target) in h:
                return h[(d, target)]
            res = 0
            for i in range(1, k + 1):
                res += dp(h, d - 1, target - i)
            h[(d, target)] = res
            return h[(d, target)]
        
        h = {}
        return dp(h, d, target) % (10 ** 9 + 7)