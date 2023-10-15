from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        """
            self.trip: consists of customerId -> (stationName, check-in-time) pairs
            self.trip_timer: consists of (checkinStation, checkoutStation) -> [trip_duration, trip_count] pairs
        """
        self.trips = {}
        self.trip_timer = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.trips[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkin_station, checkin_time = self.trips[id]
        checkout_station = stationName
        trip_duration = t - checkin_time
        route = (checkin_station, checkout_station)

        if route not in self.trip_timer:
            self.trip_timer[route] = [0, 0]

        self.trip_timer[route][0] += trip_duration
        self.trip_timer[route][1] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_duration, trip_count = self.trip_timer[(startStation, endStation)]

        return (total_duration / trip_count)
        

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)