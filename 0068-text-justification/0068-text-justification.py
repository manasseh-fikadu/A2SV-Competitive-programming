class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        if len(words) == 0:
            return []
        if len(words) == 1:
            return [words[0] + ' ' * (maxWidth - len(words[0]))]
        result = []
        i = 0
        while i < len(words):
            line = []
            line.append(words[i])
            i += 1
            while i < len(words) and len(' '.join(line)) + len(words[i]) + 1 <= maxWidth:
                line.append(words[i])
                i += 1
            if i == len(words):
                result.append(' '.join(line) + ' ' * (maxWidth - len(' '.join(line))))
            else:
                if len(line) == 1:
                    result.append(line[0] + ' ' * (maxWidth - len(line[0])))
                else:
                    space = maxWidth - len(''.join(line))
                    space_num = len(line) - 1
                    space_each = space // space_num
                    space_left = space % space_num
                    for j in range(space_left):
                        line[j] += ' ' * (space_each + 1)
                    for j in range(space_left, space_num):
                        line[j] += ' ' * space_each
                    result.append(''.join(line))
        return result