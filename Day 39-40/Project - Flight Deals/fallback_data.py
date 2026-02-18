import os
from dotenv import load_dotenv
load_dotenv()
EMAIL=  os.getenv("EMAIL")

users_fallback = [

    {"firstname": "Molly", "lastname": "Johansson", "email": EMAIL, "id": 1},
    {"firstname": "Polly", "lastname": "User", "email": EMAIL, "id": 2},
]



price_fallback = [
    {
        "city": "Paris",
        "iataCode": "PAR",
        "lowestPrice":10000,
        "id": 2
    },
    {
        "city": "Frankfurt",
        "iataCode": "FRA",
        "lowestPrice": 234.94,
        "id": 3
    },
    {
        "city": "Tokyo",
        "iataCode": "TYO",
        "lowestPrice": 551.84,
        "id": 4
    },
    {
        "city": "Hong Kong",
        "iataCode": "HKG",
        "lowestPrice": 408.61,
        "id": 5
    },
    {
        "city": "Istanbul",
        "iataCode": "IST",
        "lowestPrice": 147.14,
        "id": 6
    },
    {
        "city": "Kuala Lumpur",
        "iataCode": "KUL",
        "lowestPrice": 547.41,
        "id": 7
    },
    {
        "city": "New York",
        "iataCode": "NYC",
        "lowestPrice": 385.63,
        "id": 8
    },
    {
        "city": "San Francisco",
        "iataCode": "SFO",
        "lowestPrice": 480.64,
        "id": 9
    },
    {
        "city": "Dublin",
        "iataCode": "DBN",
        "lowestPrice": 240,
        "id": 10
    }
]
