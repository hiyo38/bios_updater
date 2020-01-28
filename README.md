## BIOS Updater

This project is made in an effort to integrate the bios updating process into the DCO work flow and make it so that all teams have access to up to date firmware.
This code parses supermicros BIOS support page and retrives all the motherboard model names and associates them with thier respective software IDs which are used to make http requests to supermicros server. 

This project uses python3.6

These Python modules are needed:
```
$ pip3 install bs4 lxml requests
```


The mobo_drivers.py file is basically done. Meanwhile the moboDB.py file is new so I have not worked on it much but it does what it needs to in order for the whole thing to work. 

TODO:
- Switch to shelve instead of sqlite DONE

- Main now takes args though its kinda hacky at the moment, its usage is like so:
```
$./main X9SCL-F X8SIL-F [....]
```
You can add all the motherboards you want to download on the command line and it will attpempt to find them in the database and then download them in sequential order.