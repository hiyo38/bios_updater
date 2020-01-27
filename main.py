#!/usr/bin/python3

import mobo_drivers
import moboDB
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download given firmware from model name')
    parser.add_argument('Model Name', nargs='*') 
    args = parser.parse_args()
    temp=vars(args).values()
    names=[]
    for i in temp:
       for name in i:
            names.append(name)	
    # Scrapes web page for names and software IDs
    modelList = mobo_drivers.get_motherboard_list()
    # Creates data base
    moboDB.createDB()
    # Takes list created by get_motherboard_list and generates rows in the DB
    moboDB.addMOBOS(modelList)
    # Query DB with model name, returns ID
    softwareID = moboDB.getMOBO(*names)
    # Pass in name and software ID to download the firmware
    mobo_drivers.download_firmware(names, softwareID)
