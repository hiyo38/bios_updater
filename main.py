#!/usr/bin/python3
import mobo_drivers
import moboDB
# import moboDB

if __name__ == "__main__":
    name = "X9SCL-F"
    # Scrapes web page for names and software IDs
    modelList = mobo_drivers.get_motherboard_list()
    # # Creates data base
    moboDB.createDB()
    # # Takes list created by get_motherboard_list and generates rows in the DB
    moboDB.addMOBOS(modelList)
    # Query DB with model name, returns ID
    softwareID = str(moboDB.getMOBO(name))
    # Pass in name and software ID to download the firmware
    mobo_drivers.download_firmware(name, softwareID)
