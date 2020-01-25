**BIOS Updater**
This project is made in an effort to integrate the bios updating process into the DCO work flow and make it so that all teams have access to up to date firmware.
This code parses supermicros BIOS support page and retrives all the motherboard model names and associates them with thier respective software IDs which are used to make http requests to supermicros server. A mysqlite database is created in the moboDB class to store this information and the mobo_drivers class uses it to download the motherboard requsted.

To use project install:

pip install bs4

pip install dataset

yum install sqlite

This project uses python3.6

The mobo_drivers.py file is basically done. Meanwhile the moboDB.py file is new so I have not worked on it much but it does what it needs to in order for the whole thing to work. There might be an issue with writing to the DB once its been created but I am currently working on it.

