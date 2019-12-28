from lxml import html
import requests, zipfile, io, bs4
import pandas as pd
import urllib
import os
import re
import subprocess
import shutil
#bashCommand = "dmidecode -r 1 | grep Product\ Name:"
#moboModel = subprocess.check_output([bashCommand])

#for line in moboModel:
#	print(line)

# Main URL I will be working from
url = r'https://www.supermicro.com/support/resources/bios_ipmi.php?type=BIOS'
#Open a connection
connection = urllib.request.urlopen(url)


def test():
    res = requests.get(url)
    res.raise_for_status()
    bios = bs4.BeautifulSoup(res.text,'lxml')
    tablehead = bios.find('table')
    tablerows = tablehead.find_all('tr')
    for tr in tablerows:
        td = tr.find_all("td", {"align" : "left"})
        a = td.find_all("a")
        if td:
            print(a[0].string)

def softwareIDList():
    # List for storing software IDs
    SoftwareItemID = []
    temp = []
    #Read the HTML from the URL
    dom = html.fromstring(connection.read())

    #Grab all the links on the page
    for link in dom.xpath('//a/@href'):
        #Regex string to caputre all software IDs at the end of links
        result = re.match(r"/about/policies/disclaimer.cfm\?SoftwareItemID=(\d*)",link)

        if(result):
            temp.append(result.group(1))
            #print(result.group(1))

    for ID in temp:
        if ID not in SoftwareItemID:
            SoftwareItemID.append(ID)
            #print(ID)
    return SoftwareItemID       

def moboModelsList():
    table = pd.read_html(url)
    #print(table[0]['Model'])
    models = table[0]['Model'].tolist()
    return models

    # This function downloads all 416 bios firmware files from the website and attempts to place them in a properly named folders.
    # In the future this function would ideally be given just the software ID after the server MOBO model has been obtained then matched with 
    # a model in the MOBO DB which would return the software ID and call this function and the naming of the folders wouldnt matter.
    # For now it is handed a list of models and softwareIDs which should be parallel lists as the model list is used purely for naming the folders they go in. The current method 
    # of obtaining the models isnt ideal but I cant seem to find a better way at the moment. The current way of parsing the Models only works for about 80% of them.
    # There are certain edge cases where it just doesnt work but in reality we only need about a dozen motherboards and they arent effected. 
def downloadFirmware(model,softwareID): 
    #Create the path for the dir
    path  = os.getcwd() + "/BIOS"
    
    try:
        shutil.rmtree("BIOS")
        os.mkdir(path)
        print("Creating BIOs dir")
    except OSError:
        print("Failed to create BIOS folder")

    for i,ID in enumerate(softwareID):
        os.system('clear')
        print("Downloading Firware ["+ str(i+1) +"/"+ str(len(softwareID))+"]")
        start = model[i][0] 
        if(start != 'A'or start != 'C'):
            models = model[i].split(start)
            del(models[0])
            print(models)
            r = requests.get("https://www.supermicro.com/support/resources/getfile.php?SoftwareItemID="+ID, stream=True)
            z = zipfile.ZipFile(io.BytesIO(r.content))
            for names in models:
                z.extractall(path+"/"+start+names)
        
        

    return
