# PYIPMI

This script can control fans with ipmi.

## Important ##

You have to install `ipmitool` before you can use this script!
 
 ###### Debian/Ubuntu 
`sudo apt install ipmitool`
 ###### Fedora
`sudo dnf install ipmitool`
 ###### Arch
`sudo pacman -S ipmitool`


## Usage

`python3 ipmi.py`

## Features
```
Turn off Automatic ventilation control.
Turn on Automatic ventilation control.
Set fans to 25% speed.
Set fans to 50% speed.
Set fans to 75% speed.
Set fans to 100% speed.
Set fans to custom speed.
Turn off All fans.
```

## Working with:
All Dell poweredge server!
## Tested on:
```
Dell Poweredge R410
Dell Poweredge R510
Dell Poweredge R710
Dell Poweredge R720
```

## OS Support:
In theory Support all linux system!
## Tested on:
```
Kali Linux
Kali Nethunter
Linux Lite
Ubuntu 20.04
Debian
MX Linux
Arch
```
## Unsupported:
```
Termux
```
