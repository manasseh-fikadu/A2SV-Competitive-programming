class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        # Scan from left to right and greedily match a locked ')' to an earlier locked '('.
        # If running out of locked '(', start consuming unlocked.
        # Once all ')' paired, from right to left, pair locked '(' with unlocked.
        # After all locked processed, return True since the rest unlocked can always be manipulated to keep the string valid.
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