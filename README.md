##BIOS Updater

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
- Have main take in args to change the name of the model that needs to be downloaded