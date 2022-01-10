from typing import Text
from phue import Bridge
import time
import requests
from sense_hat import SenseHat


response = requests.get('https://api.coingecko.com/api/v3/coins/ethereum?tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false')
eth_price= response.json()
#print(eth_price['price_change_percentage_1h_in_currency'])
eth_market_data = eth_price['market_data']['price_change_percentage_1h_in_currency']['usd']
print(type(eth_market_data))

red_message = sense.show_message("Market is fucked", text_colour =[255,0,0])
green_message = sense.show_message("Market is mooning", text_colour =[0,255,0])

#bridge_ip_address = '192.168.1.2'
#b = Bridge(bridge_ip_address)


#if eth_market_data > 0.0:
    #green_lights()

#elif eth_market_data < 0.0:
   #red_lights()
red_message()
green_message()
#print(eth_market_data)


    

