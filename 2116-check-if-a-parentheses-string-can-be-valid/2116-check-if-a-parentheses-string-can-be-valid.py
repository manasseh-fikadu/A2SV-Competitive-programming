class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False

        locked_n_open = []
        unlocked = []
        
        for i, brace in enumerate(s):
            if locked[i] == '0':
                unlocked.append(i)
            else:
                if brace == '(':
                    locked_n_open.append(i)
                else:
                    if locked_n_open:
                        locked_n_open.pop()
                    elif unlocked:
                        unlocked.pop()
                    else:
                        return False
        
        while locked_n_open:
            if unlocked and unlocked[-1] > locked_n_open[-1]:
                unlocked.pop()
                locked_n_open.pop()
            else:
                return False
        return True