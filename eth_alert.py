#from typing import Text
from phue import Bridge
import time
import requests
#from sense_hat import SenseHat

def get_market_data():
    response = requests.get('https://api.coingecko.com/api/v3/coins/ethereum?tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false')
    eth_price= response.json()
    eth_market_data = eth_price['market_data']['price_change_percentage_1h_in_currency']['usd']
    eth_market_data = ("%.2f" % eth_market_data)
    return eth_market_data

def matrix_display(eth_market_data):
    sense = SenseHat()
    red_message = sense.show_message(
        "Market is fucked, ETH is down {} % in the past hour".format(get_market_data()), 
        text_colour =[255,0,0])
    green_message = sense.show_message(
        "Market is mooning, ETH is up {} % in the hour".format(get_market_data()), 
        text_colour =[0,255,0])

    if eth_market_data() > 0.0:
        return green_message
    elif eth_market_data() < 0.0:
        return red_message
