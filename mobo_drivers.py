#!/usr/bin/python3

import io
import os
import re
import shutil
import zipfile

import bs4
import requests

from config import get_config


def get_motherboard_list() -> list:
    """
    This does everything now. Returns a list of lists formatted like this
    [['moboName1','moboName2','softwareID'],['moboName1','moboName2','softwareID']...,] .
    All the motherboards in a list have the same softwareID in common making it easy for them to group together.
    @return: list
    """
    # request page
    tries = 0
    while tries < get_config("SETTINGS", "MAX_RETRIES"):
        res = requests.get(get_config("SETTINGS", "BIOS_URL"))
        if res.status_code != 200:
            tries += 1
            continue
        break
    # parse page
    bios = bs4.BeautifulSoup(res.text, "lxml")
    table_head = bios.find("table")
    tr = table_head.find_all("tr")
    models = []
    for text in tr:
        model_info = []
        links = text.find_all("a")
        for mobo in links:
            result = re.match(
                r"/about/policies/disclaimer.cfm\?SoftwareItemID=(\d*)",
                mobo.get("href"),
            )
            if result:
                model_info.append(int(result.group(1)))
            for name in mobo:
                if validate(name):
                    model_info.append(name)
        if model_info:
            models.append(model_info)
    return models


def validate(item: str) -> bool:
    """
    @param item:
    @return:
    """
    for exclusion in get_config("SETTINGS", "EXCLUDED_FILES"):
        if exclusion in item.lower():
            return False
    return True


# Pass in two args. The model arg is the name of the folder that the BIOS will be placed in
# The softwareID is appended to a http request that get the firmware from the supermicro database
def download_firmware(model, software_id) -> None:
    """
    Downloads model firmware to target directory
    @param model: list
    @param software_id: list,int
    @return:
    """
    # Create the path for the dir
    path = os.getcwd() + "/BIOS"
    URL = (
        "https://www.supermicro.com/support/resources/getfile.php?SoftwareItemID="
        
    )

    try:
        shutil.rmtree("BIOS")
        print("Deleting old BIOS dir")
    except OSError:
        print("No old BIOS dir Found")
    try:
        os.mkdir(path)
        print("Creating BIOS dir")
    except OSError:
        print("Failed to create BIOS dir")
    if isinstance(software_id,list):
       for i in range(len(software_id)):	
           r = requests.get(URL+str(software_id[i]), stream=True)
           z = zipfile.ZipFile(io.BytesIO(r.content))
           z.extractall(path + "/" + model[i])
           print("Downloaded firmware for " + model[i]+ " motherboard")
    else:
         r = requests.get(URL+str(software_id), stream=True)
         z = zipfile.ZipFile(io.BytesIO(r.content))
         z.extractall(path + "/" + model[0])
         print("Downloaded firmware for " + model[0]+ " motherboard")

    return
