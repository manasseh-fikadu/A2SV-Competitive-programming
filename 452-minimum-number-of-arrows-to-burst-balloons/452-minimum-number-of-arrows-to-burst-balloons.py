class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
                        Fire           Fire
          1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16
        --|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--
          |__|___________|  |  |     |     |           |
             |______________|__|     |     |           |
                            |________|_____|           |
                                     |_________________|
        '''
        points.sort(key = lambda p: p[1])
        ans, arrow = 0, 0
        for [start, end] in points:
            if ans == 0 or start > arrow:
                ans, arrow = ans + 1, end
        return ans