## BIOS Updater

This code parses supermicros BIOS support page and retrives all the motherboard model names and associates them with thier respective software IDs which are used to make http requests to supermicros server.

This project uses python3.6

These Python modules are needed:
```
$ pip3 install bs4 lxml requests python-magic
```
or
```
$ pip3 install -r requirements.text
```
which is recommended

Updater takes args and its usage is like so:
```
$./updater.py X9SCL-F X8SIL-F [....]
```
You can add all the motherboards you want to download on the command line, it will then attempt to find them in the database and download them in sequential order.

updater.py also has a default state when given no args. It looks for a file name "motherboards.txt" and uses the models found in it to download a set list of roms.

The program is now able to automate the whole installation process by typing
```
$ ./updater.py auto
```
It will parse the server hardware information for the motherboard and then make a request to the data base with the model name and attempt to download the rom and install.

One folder is generated called ROMS which stores the roms downloaded by the updater. All ROM data is cached in the .frimware shelf database and is downloaded as needed.  
