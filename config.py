#!/usr/bin/python3
import json


def get_config(block, key):
    with open("config.json") as config:
        data = json.load(config)
    return data[block][key]
