class MyCalendarThree:
    def __init__(self):
        self.calendar = []
        self.overlap = 0

    def book(self, start: int, end: int) -> int:
        self.calendar.append((start, 1))
        self.calendar.append((end, -1))
        self.calendar.sort()
        count = 0
        for _, val in self.calendar:
            count += val
            self.overlap = max(self.overlap, count)
        return self.overlap
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)