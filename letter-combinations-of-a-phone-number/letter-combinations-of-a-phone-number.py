class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        
        if not digits or '0' in digits or '1' in digits:
            return  []
        
        results = [[]]
        
        for digit in digits:
            temp = []
            for result in results:
                for letter in mapping[digit]:
                    temp.append(result + [letter])
            results = temp
            
        return ["".join(result) for result in results]
        