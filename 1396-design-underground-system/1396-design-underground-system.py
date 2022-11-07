class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.pairs = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkin[id]
        self.checkin.pop(id)
        self.pairs[(startStation, stationName)] = self.pairs.get((startStation, stationName), []) + [t - startTime]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.pairs[(startStation, endStation)]
        return sum(times) / len(times)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)