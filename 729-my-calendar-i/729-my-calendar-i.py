class MyCalendar:

    def __init__(self):
        self.cal = []

    def book(self, start: int, end: int) -> bool:
        l, r = 0, len(self.cal)

        if self.cal:
            while l < r:
                mid = (l+r) // 2
                if end == self.cal[mid][0]:
                    l = mid
                    break
                elif end > self.cal[mid][0]:
                    l = mid + 1
                else:
                    r = mid
		
        if l-1 >= 0:
            if start < self.cal[l-1][1]:
                return False
        
        self.cal.insert(l, (start, end))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)