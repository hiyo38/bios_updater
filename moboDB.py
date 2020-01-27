#!/usr/bin/python3
import mobo_drivers
import shelve


def createDB():  # This function technically isn't needed, as shelve creates a database as necessary.
    with shelve.open(".firmware") as _:
        pass


def getDB():
    with shelve.open(".firmware") as db:
        for model in db:
            print("{}: {}".format(model.ljust(20), db[model]))
    return None


def addMOBOS(motherboardList):
    with shelve.open(".firmware") as db:
        for modelList in motherboardList:
            ID = modelList[-1]
            for model in modelList:
                if isinstance(
                    model, str
                ):  # making sure that the Software ID isn't pulled
                    db[model] = ID


# Method that returns data to you based on what you put in. For example if give a motherboard string it will return any software ID associated with it in the database.
# If you give it an int software ID it will return all MOBOS associated with it in the db
def getMOBO(*args):
    retls = []
    with shelve.open(".firmware") as db:
        for model in args:
            print("Searching for {}...".format(model))
            if model in db:
                print("{}: {}".format(model.ljust(20), db[model]))
                retls.append(db[model])
            else:
                print("Motherboard {} not found in database".format(model))

    if len(args) <= 1:  # Returns list of software ID's if more than one arg is given
       return retls[0]
    else:
       return retls

if __name__ == "__main__":

    getMOBO("370DLR")
    getDB()
