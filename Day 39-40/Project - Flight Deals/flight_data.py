import datetime as dt




class FlightData():
    def __init__(self):
       super().__init__()
       self.price = "N/A"
       self.origin_airport = "N/A"
       self.destination_airport = "N/A"
       self.departure_time="N/A"
       self.departure_date = (dt.datetime.now() + dt.timedelta(days=1)).strftime("%Y-%m-%d")
       self.return_date = (dt.datetime.now() + dt.timedelta(days=30)).strftime("%Y-%m-%d")
       self.is_direct=False
       self.stops = "N/A"


    # Hittar den billigaste flygresan och uppdaterar pris och avgångstid
    def find_cheapest_flight(self, data=None):

        if   len(data) >= 1 :

               for item in range(len(data)):
                   if self.price == "N/A" or float(data[item]["price"]["total"]) and float(
                           data[item]["price"]["total"]) < float(self.price):

                       self.price = float(data[item]["price"]["total"])
                       date = data[item]["itineraries"][0]["segments"][0]["departure"]["at"]
                       self.departure_time = date.split("T")[1][:5]

                       nr_stops = len(data[item]["itineraries"][0]["segments"]) - 1
                       self.stops= nr_stops
                       self.destination_airport = data[item]["itineraries"][0]["segments"][nr_stops]["arrival"]["iataCode"]

        else:
               print(f"❌ No flights: {self.origin_airport} - {self.destination_airport} ")











