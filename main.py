import mobo_drivers as Drivers
import moboDB as Database
if __name__ == "__main__":
    name = "X9SCL-F"
    # Scrapes web page for names and software IDs
    ModelList = Drivers.get_motherboard_list()
    # Creates data base
    Database.createDB()
    # Takes list created by get_motherboard_list and generates rows in the DB 
    Database.addMOBOS(ModelList)
    # Query DB with model name, returns ID
    softwareID = Database.getMOBO(name)
    # Pass in name and software ID to download the firmware
    Drivers.download_firmware(name,softwareID)
