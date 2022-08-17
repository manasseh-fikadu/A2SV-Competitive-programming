class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mapping = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        morse = set()
        
        for word in words:
            transformation = ""
            for char in word:
                transformation += mapping[ord(char)-97]
            morse.add(transformation)
            print(morse)
                
        return len(morse)
                