#!/usr/bin/env python3

from utils import get_json

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

a = get_json(url)

print(a)
