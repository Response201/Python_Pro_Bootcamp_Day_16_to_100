from data_manager import DataManager


get_func = DataManager()



def check_flights():


    for row in get_func.data:
        # Skriv ut startpris och IATA-kod för debugging
        print("START PRICE:", row["lowestPrice"], row["iataCode"])

        get_func.price = row["lowestPrice"]   # Nuvarande lägsta pris för jämförelse
        get_func.origin_airport = "MAD"
        get_func.destination_airport = row["iataCode"]

        # Hitta det billigaste flyget för denna rutt
        # Om ett nytt lägsta pris hittas uppdateras get_func.price
        get_func.find_cheapest_flight()

        # Om det nya priset är lägre än det gamla lägsta priset -> skicka sms och uppdatera excel-filen
        if row["lowestPrice"] > get_func.price:

            get_func.send_sms()
            get_func.update_exel(row["id"], get_func.price)



check_flights()

