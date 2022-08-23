class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while target > 1:
            if target % 2 == 0 and maxDoubles > 0:
                maxDoubles -= 1
                target = int(target / 2)
            elif target % 2 == 1:
                target -= 1
            else:
                moves += target - 1
                target = 0
                break
            moves += 1
        return moves
                