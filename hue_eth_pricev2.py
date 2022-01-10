from phue import Bridge
import time
import requests


response = requests.get('https://api.coingecko.com/api/v3/coins/ethereum?tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false')
eth_price= response.json()
#print(eth_price['price_change_percentage_1h_in_currency'])
eth_market_data = eth_price['market_data']['price_change_percentage_1h_in_currency']['usd']
print(type(eth_market_data))

bridge_ip_address = '192.168.1.2'
b = Bridge(bridge_ip_address)


def access_lights(bridge_ip_address):
    b = Bridge(bridge_ip_address)
    light_names_list = b.get_light_objects('name')
    print(light_names_list)
    return light_names_list

def market_lights():
    lights = access_lights(bridge_ip_address)
    for light in lights:
        lights[light].on = True
        lights[light].hue = 180
        lights[light].saturation = 100

access_lights(bridge_ip_address)
market_lights()

def white_lights():
    lights = access_lights(bridge_ip_address)
    for light in lights:
        lights[light].on = True
        lights[light].hue = 25500
        lights[light].saturation = 100

def lights_on():
    lights = access_lights(bridge_ip_address)
    for light in lights:
        lights[light].on = True

def red_lights():
    lights = access_lights(bridge_ip_address)
    count = 0
    while (count < 5):
        for light in lights:
            lights[light].on = True
            lights[light].hue = 180
            lights[light].saturation = 250
            time.sleep(.3)
            lights[light].on= False
            count = count + .3

def green_lights():
    lights = access_lights(bridge_ip_address)
    count = 0
    while (count < 5):
        for light in lights:
            lights[light].on = True
            lights[light].hue = 25500
            lights[light].saturation = 250
            time.sleep(.3)
            lights[light].on= False
            count = count + .3

if eth_market_data > 0.0:
    green_lights()

elif eth_market_data < 0.0:
   red_lights()
print(eth_market_data)

lights_on()

    

