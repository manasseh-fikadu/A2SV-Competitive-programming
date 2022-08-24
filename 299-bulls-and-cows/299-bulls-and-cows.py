class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        i = 0
        j = 0

        secrets = [k for k in secret]
        guesses = [k for k in guess]
            
        for k in range(len(secret)):
            if secret[k] == guess[k]: 
                i += 1
                secrets.remove(secret[k])
                guesses.remove(guess[k])
                
        for k in range(len(guesses)):
            if guesses[k] in secrets:
                j += 1
                secrets.remove(guesses[k])

        res = str(i) + "A" + str(j) + "B"

        return res
