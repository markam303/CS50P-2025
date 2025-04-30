### Bitcoin Price Index ###
import sys
import requests
import json


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: bitcoin.py <float>")
    
    API_key = "4862c850dd068878bacc7bd19ca8c5395806430360b8fbb48597a48bd2cf52ad"
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=" + API_key)
    
    o = response.json()
    for data in o["data"]:
        print(data["priceUsd"])
    
    # print(f"${amount:,.4f}")
        
if __name__ == "__main__":
    main()