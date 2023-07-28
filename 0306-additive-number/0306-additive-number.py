class Solution:
    def isAdditiveNumber(self, num: str):
        path = []

        def backtrack(current, size) -> bool:
            if size >= 3 and path[-1] != path[-2] + path[-3]:
                return False

            if current == '':
                return size >= 3

            for cur_idx in range(1, len(current) + 1):
                cur_str, remain = current[:cur_idx], current[cur_idx:]

                if cur_str.startswith('0') and cur_str != '0':
                    break

                path.append(int(cur_str))

                if backtrack(remain, size + 1): 
                    return True

                path.pop()

            return False

        return backtrack(num, 0)