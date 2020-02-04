## BIOS Updater

This project is made in an effort to integrate the bios updating process into the DCO work flow and make it so that all teams have access to up to date firmware.
This code parses supermicros BIOS support page and retrives all the motherboard model names and associates them with thier respective software IDs which are used to make http requests to supermicros server. 

This project uses python3.6

These Python modules are needed:
```
$ pip3 install bs4 lxml requests
```
Updater now takes args though its kinda hacky at the moment, its usage is like so:
```
$./updater.py X9SCL-F X8SIL-F [....]
```
You can add all the motherboards you want to download on the command line, it will then attempt to find them in the database and download them in sequential order.
updater.py now has a default state when given no args. It looks for a file name "motherboards.txt" and uses the models found in it to download a set list of roms.
TODO:
- Switch to shelve instead of sqlite DONE
- Have the whole program use SUM to automate updating bios and retriving the latest versions all dynamically.