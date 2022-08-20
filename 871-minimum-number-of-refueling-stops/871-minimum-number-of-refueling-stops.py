class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stops = 0
        fuel = startFuel
        past_fuels = []
        stations.append([target, 0])

        for location, station_fuel in stations:
            while fuel < location:
                if not past_fuels:
                    return -1

                fuel -= heapq.heappop(past_fuels)
                stops += 1
            heapq.heappush(past_fuels, -station_fuel)

        return stops