### Bitcoin Price Index ###
import sys
import requests
import json


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    
    API_key = "4862c850dd068878bacc7bd19ca8c5395806430360b8fbb48597a48bd2cf52ad"
    url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey="
    response = requests.get(url + API_key)
    
    o = response.json()
    price = float(o["data"]["priceUsd"])

    amount = price * n
    
    print(f"${amount:,.4f}")
        
if __name__ == "__main__":
    main()