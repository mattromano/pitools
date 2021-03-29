# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from phue import Bridge
import time


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

#access_lights(bridge_ip_address)
#market_lights()

def white_lights():
    lights = access_lights(bridge_ip_address)
    for light in lights:
        lights[light].on = True
        lights[light].hue = 25500
        lights[light].saturation = 100
        
"""def red_lights():
    lights = access_lights(bridge_ip_address)
    for light in lights:
        lights[light].on = True
        lights[light].hue = 180
        lights[light].saturation = 200"""
        
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



red_lights()
#if __name__ = '__main__':
    

