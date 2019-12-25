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
        for mobo in td:
            print(mobo.string)
    return

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
        
        models = model[i].split(start)
        print(models)
        r = requests.get("https://www.supermicro.com/support/resources/getfile.php?SoftwareItemID="+ID, stream=True)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        for names in models:
            z.extractall(path+"/"+start+names)
        
        

    return
