#!/usr/bin/python3
import json
import os

def get_config(block, key):
    with open(os.path.dirname(__file__)+'/config.json') as config:
        data = json.load(config)
    return data[block][key]
