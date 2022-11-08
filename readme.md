# Keyper
> Written by OpSec WareHouse LLC (opsec.sh/market)

## Features
- Support for both CLI and GUI
- Encrypted local database storage
- Random password generator (adjustable complexity levels)
- Database backup to [cryptobin.co](https://cryptobin.co)
- Preventing memory leaks

## Installation
Install Python Dependencies
```
python -m pip install -r requirements.txt
```

## Usage
There are numerous function commands!
```
# Core
~$ python ./keyper.py --update
~$ python ./keyper.py --gui

# Main Fun
~$ python ./keyper.py --create # creates a new database
~$ python ./keyper.py --changepwd # change master db passwd
~$ python ./keyper.py --export # export all creds stored in db

# DB Fun
~$ python ./keyper.py --add_alias test@example.com | ~$ python ./keyper.py --add_alias username1
```

## Code Structure

### keyperlib
```
MainCore -> Handler for CLI/GUI interaction
DataCore -> Handler for database interactions
GUICore  -> Handler for GUI functionality
UtilCore -> Helper functions for internal code
```
