import sortedcontainers
class MyCalendar:

    def __init__(self):
        self.calendar = sortedcontainers.SortedDict()
        

    def book(self, start: int, end: int) -> bool:
        if start in self.calendar:  return False
        index = self.calendar.bisect(start)
        if (index == 0 or (index > 0 and self.calendar[self.calendar.keys()[index - 1]] <= start)) and (index == len(self.calendar) or (index < len(self.calendar) and self.calendar.keys()[index] >= end)):
            self.calendar[start] = end
            return True
        return False
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)