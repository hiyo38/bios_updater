#!/usr/bin/python3
from MotherboardData import mobo_drivers
from MotherboardData import moboDB
import argparse
import os

if __name__ == "__main__":
    # Scrapes web page for names and software IDs
    modelList = mobo_drivers.get_motherboard_list()
    # Creates data base
    moboDB.createDB()
    # Takes list created by get_motherboard_list and generates rows in the DB
    moboDB.addMOBOS(modelList)
    parser = argparse.ArgumentParser(
        description='Download given firmware from model name')
    parser.add_argument('Model Name', nargs='*')
    # parser.add_argument('Default',nargs='?',const=1)
    args = parser.parse_args()
    temp = vars(args).values()
    names = []
    for i in temp:
        for name in i:
            names.append(name)
    try:
        if names[0] == 'auto':
            print("Detecting motherboard model....")
            mobo_drivers.auto_download()
    except:
        print("Downloading from motherboards.txt")
        if names != 'auto':
            if len(names) == 0:
                f = open(os.path.dirname(__file__) + '/MotherboardData/motherboards.txt', "r")
                motherboards = f.readlines()
                for line in motherboards:
                    names.append(line.strip())

        # Query DB with model name, returns ID
        softwareID = moboDB.getMOBO(*names)
        # Pass in name and software ID to download the firmware
        mobo_drivers.download_firmware(names, softwareID)
