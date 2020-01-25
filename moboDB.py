#!/usr/bin/python3
import mobo_drivers
import dataset
db = dataset.connect('sqlite:///Firmware.db')
def createDB():
     #db = dataset.connect('sqlite:///Firmware.db')
    db['MOBOS'].drop()
    db.create_table('MOBOS')
def deleteDB():
    
    return
def getDB():
    for mobo in db['MOBOS']:
        print(mobo['model'])
        print(mobo['SoftwareID'])
    print(db.tables)
    return

def addMOBOS(motherboardList):
    table = db.get_table('MOBOS')
    for dataset in motherboardList:
        ID = dataset[len(dataset)-1]
        for item in dataset:
            if isinstance(item,str):
               table.insert(dict(model=item,software=ID))
    return

# Method that returns data to you based on what you put in. For example if give a motherboard string it will return any software ID associated with it in the database.
# If you give it an int software ID it will return all MOBOS associated with it in the db
def getMOBO(model,*args):
    try:
        table = db.load_table('MOBOS')
    except:
        print("Table not found try creating database first")
    
    result = (table.find_one(model=model)['software'])
    # for arg in args:
    #     if isinstance(arg,str):
    #         result.append(table.find(model=arg)['SoftwareID'])
    #     if isinstance(arg,int):
    #         result.append(table.find(SoftwareID=arg)['model'])
        
    print(result)
    return result


if __name__ == "__main__":
    
    getMOBO("X11SSL-F")
    getDB()
    
    
