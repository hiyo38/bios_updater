import mobo_drivers
import sqlite3

connection = sqlite3.connect("MotherboardFirmware.db")
def createDB():
    connection = sqlite3.connect("MotherboardFirmware.db")
    
    sql_command = """
        CREATE TABLE motherboards ( 
        softwareID INT,
        model VARCHAR(30));"""
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS motherboards")
    cursor.execute(sql_command)
    print("Database Created")
    connection.close()
    return

def getDB():

    return

def addMOBO(model,ID):
    sql = "INSERT INTO motherboards(softwareID, \
    model) \
    VALUES ('%d', '%s')" % \
    (ID, model)

    connection = sqlite3.connect("MotherboardFirmware.db")
    cursor = connection.cursor()
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        connection.commit()
        print("Added mobo")
    except:
        # Rollback in case there is any error
        connection.rollback()
        print("failed to add mobo")

    # disconnect from server
    connection.close()
    return


def getMOBO():
    return


if __name__ == "__main__":
    createDB()
    addMOBO("test",5)