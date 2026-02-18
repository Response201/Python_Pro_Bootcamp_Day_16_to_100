from data_manager import DataManager

get_func = DataManager()






for row in get_func.data_prices:

        # Skriv ut startpris och IATA-kod för debugging
        print(f"\nCheck {row["iataCode"]} \nCurrent lowest price: {row["lowestPrice"]}")

        get_func.price = row["lowestPrice"]   # Nuvarande lägsta pris för jämförelse
        get_func.origin_airport = "LON"
        get_func.destination_airport = row["iataCode"]

        # Hitta det billigaste flyget för denna rutt
        # Om ett nytt lägsta pris hittas uppdateras get_func.price
        get_func.check_flights()

        # Om det nya priset är lägre än det gamla lägsta priset -> skicka sms, email och uppdatera excel-filen
        if row["lowestPrice"] > get_func.price:

            get_func.send_sms()
            get_func.send_mail()
            get_func.update_exel( row_id=row["id"], new_price = get_func.price)





