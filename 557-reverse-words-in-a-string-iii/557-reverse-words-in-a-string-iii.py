class Solution:
    def reverseWords(self, s: str) -> str:
        split_list = list(s.split(' '))
        for i in range(len(split_list)):
            split_list[i] = split_list[i][::-1]
        return " ".join(split_list)