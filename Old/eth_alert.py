#!/usr/bin/env python2
from time import sleep
import requests
from sense_hat import SenseHat


def get_market_data():
    response = requests.get(
        "https://api.coingecko.com/api/v3/coins/ethereum?tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false"
    )
    eth_price = response.json()
    eth_market_data = eth_price["market_data"][
        "price_change_percentage_1h_in_currency"
    ]["usd"]
    eth_market_data = "%.2f" % eth_market_data
    return eth_market_data


w = (150, 150, 150)
g = (0, 255, 0)
r = (255, 0, 0)
e = (0, 0, 0)

up_only_arrow = [
    e,
    e,
    e,
    g,
    g,
    e,
    e,
    e,
    e,
    e,
    g,
    g,
    g,
    g,
    e,
    e,
    e,
    g,
    e,
    g,
    g,
    e,
    g,
    e,
    g,
    e,
    e,
    g,
    g,
    e,
    e,
    g,
    e,
    e,
    e,
    g,
    g,
    e,
    e,
    e,
    e,
    e,
    e,
    g,
    g,
    e,
    e,
    e,
    e,
    e,
    e,
    g,
    g,
    e,
    e,
    e,
    e,
    e,
    e,
    g,
    g,
    e,
    e,
    e,
]

down_only_arrow = [
    e,
    e,
    e,
    r,
    r,
    e,
    e,
    e,
    e,
    e,
    r,
    r,
    r,
    r,
    e,
    e,
    e,
    r,
    e,
    r,
    r,
    e,
    r,
    e,
    r,
    e,
    e,
    r,
    r,
    e,
    e,
    r,
    e,
    e,
    e,
    r,
    r,
    e,
    e,
    e,
    e,
    e,
    e,
    r,
    r,
    e,
    e,
    e,
    e,
    e,
    e,
    r,
    r,
    e,
    e,
    e,
    e,
    e,
    e,
    r,
    r,
    e,
    e,
    e,
]


def matrix_display(eth_market_data):
    sense = SenseHat()

    if float(eth_market_data) > 0.0:
        sense.set_pixels(up_only_arrow)
        sleep(5)
        sense.show_message(
            "Market is mooning, ETH is up {} % in the hour".format(get_market_data()),
            text_colour=[0, 255, 0],
        )

    elif float(eth_market_data) < 0.0:
        sense.set_rotation(180)
        sense.set_pixels(down_only_arrow)
        sleep(5)
        sense.set_rotation(180)
        sense.show_message(
            "Market is fucked, ETH is down {} % in the past hour".format(
                get_market_data()
            ),
            text_colour=[255, 0, 0],
        )


matrix_display(get_market_data())
