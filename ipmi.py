#!/usr/bin/env python3

import bcrypt
import os,sys
import time,json
from getpass import getpass

## Colors ##

GREEN = "32m"
RED   = "31m"
YELLOW = "33m"

def color_text(color, text):
    colored_text = f"\033[{color}{text}\033[00m"
    return colored_text

## Config ##

def config(filename):
    try:
       with open(filename) as config_file:
            data = json.load(config_file)
            return data

    except FileNotFoundError as e:
        e.strerror = "Config file not found!"
        raise e

try:
    config("config.json")

## Config not found ## 

except FileNotFoundError as e:
    print(e)
    time.sleep(0.3)
    a = input("Do you want to create now? (Y/N) ")

    Yes = (['yes','Yes','Y','y'])
    No = (['No', 'no', 'N', 'n'])

    if a in Yes:
        os.system('python3 hash.py')
        time.sleep(0.3)
        sys.exit()
    elif a in No:
        print('Exit...')
        time.sleep(0.3)
        sys.exit()
    else:
        sys.exit()

password = getpass().encode('utf-8')

## Config ##

data = config("config.json")

ip = data['ip']
user = data['user']
hashedpasswd = data['pass'].encode("utf-8")

## ipmi ##

def ipmitool(args):
    os.system('ipmitool -I lanplus -H ' + ip + ' -U ' + user + ' -P ' + password.decode('utf-8') + ' raw ' + args + ' 2>/dev/null' )
    return '1'

def custom_ipmi(args):
    os.system('ipmitool -I lanplus -H ' + ip + ' -U ' + user + ' -P ' + password.decode('utf-8') + ' raw ' + '0x30 0x30 0x02 0xff 0x' + args + ' 2>/dev/null' )
    return '1'

## Menu1 ##

def main_menu():
    menu = 30 * "-" + "MENU" + 30 * "-"
    print (color_text(GREEN,menu))
    print (22 * ' ' + ' ' + "(1) Fan control"   )
    print (22 * ' ' + ' ' + "(2)" + 4 * ' ' + "More"   )
    print (23 * ' ' + "(99)" + 3 * ' ' + "Quit")
    print (color_text(GREEN,64 * "-"))

## MEnu2 ##

def fan_menu():
        menu = 25 * "-" + "Fan Control MENU" + 22 * "-"
        print (color_text(GREEN,menu))
        print (16 * ' ' + "(1)" + " Turn off automatic fan control")
        print (16 * ' ' + "(2)" + 6 * ' ' + "Set Fan speed to 25%" )
        print (16 * ' ' + "(3)" + 6 * ' ' + "Set Fan speed to 50%" )
        print (16 * ' ' + "(4)" + 6 * ' ' + "Set Fan speed to 75%" )
        print (16 * ' ' + "(5)" + 6 * ' ' + "Set Fan speed to 100%" )
        print (16 * ' ' + "(6)" + 7 * ' ' + "Custom speed(0-100)" )
        print (16 * ' ' + "(98)" + 11 * ' ' + "Back")
        print (16 * ' ' + "(99)" + 11 * ' ' + "Quit")
        print (color_text(GREEN,64 * "-"))

## Menu 3 ##

def more_menu():
    menu = 27* "-" + "More MENU" + 28 * "-"
    print (color_text(GREEN,menu))
    print (14 * ' ' + ' ' + "(1) Turn on automatic fan control"   )
    print (14 * ' ' + ' ' + "(2)" + 6 * ' ' + "Turn off " + (color_text(RED,'all')) + " fans"   )
    print (15 * ' ' + "(98)" + 11 * ' ' + "Back")
    print (15 * ' ' + "(99)" + 11 * ' ' + "Quit")
    print (color_text(GREEN,64 * "-"))

## hashed pass ##

if bcrypt.checkpw(password, hashedpasswd):
    stat = 1
else:
    stat = 0

if stat == 1:
    os.system('clear')
    time.sleep(0.01)
    fd435 = "Password OK"
    okpsw = 27 * "-" + (color_text(GREEN,fd435)) + (color_text(GREEN,26 * "-")) 
    print (color_text(GREEN,okpsw))
    time.sleep(0.1)
    Quit = ['99', 'Q', 'q', 'Quit', 'quit']
    loop = True
    while loop:
        main_menu()
        ans = input(color_text(GREEN,"Select: "))

        if ans == '1':
            os.system('clear')
            fan_menu()
            inp = input(color_text(GREEN,"Select: "))

            if inp == '1':
                os.system('clear')
                ipmitool('0x30 0x30 0x01 0x00')
                print(color_text(YELLOW,17 * "-" + "Automatic Fan control turned off" + 14 * "-"))

            elif inp == '2':
                os.system('clear')
                ipmitool('0x30 0x30 0x02 0xff 0x19')
                print(color_text(YELLOW,23 * "-" + "Fan Speed set to 25%" + 21 * "-"))

            elif inp == '3':
                os.system('clear')
                ipmitool('0x30 0x30 0x02 0xff 0x32')
                print(color_text(YELLOW,23 * "-" + "Fan Speed set to 50%" + 21 * "-"))

            elif inp == '4':
                os.system('clear')
                ipmitool('0x30 0x30 0x02 0xff 0x4b')
                print(color_text(YELLOW,23 * "-" + "Fan Speed set to 75%" + 21 * "-"))

            elif inp == '5':
                os.system('clear')
                ipmitool('0x30 0x30 0x02 0xff 0x64')
                print(color_text(YELLOW,22 * "-" + "Fan Speed set to 100%" + 21 * "-"))

            elif inp == '6':
                loop2 = True
                while loop2:
                    os.system('clear')
                    print (color_text(GREEN,27 * "-" + "Custom speed" + 25 * "-"))
                    inp = input(color_text(GREEN,"> "))
                    try:
                        if int(inp) in range(0, 101):
                            output = hex(int(inp)).split('x')[-1]
                            custom_ipmi(output)
                            if output == '64':
                                os.system('clear')
                                print(color_text(YELLOW,22 * "-" + "Fan Speed set to 100%" + 21 * "-"))
                                loop2 = False
                            else:
                                os.system('clear')
                                print(color_text(YELLOW,23 * "-" + "Fan Speed set to " + inp + "%" + 21 * "-"))
                                loop2 = False

                        elif inp == '999':
                            os.system('clear')
                            loop2 = False

                        else:
                            os.system('clear')
                            print(color_text(RED,16 * "-" + "Select a number between 0 and 100" + 15 * "-"))
                            time.sleep(1.4)
                            loop2 = True
                    except ValueError:
                        os.system('clear')
                        print(color_text(RED,21 * "-" + "Only numbers are allowed" + 19 * "-"))
                        time.sleep(1.4)
                        loop2 = True
            
            elif inp == '98':
                os.system('clear')

            elif inp in Quit:
                os.system('clear')
                print (color_text(GREEN,30 * "-") + (color_text(RED,'Quit')) + (color_text(GREEN,30 * "-")))
                time.sleep(0.1)
                loop = False
            
            else:
                os.system('clear')
                print(color_text(GREEN,26 * "-") + (color_text(RED,'Invalid Input')) + (color_text(GREEN,25 * "-")))
                time.sleep(0.2)
                loop = True

        
        elif ans == '2':
            os.system('clear')
            more_menu()
            inp2 = input(color_text(GREEN,"Select: "))

            if inp2 == '98':
                os.system('clear')

            elif inp2 in Quit:
                os.system('clear')
                print (color_text(GREEN,30 * "-") + (color_text(RED,'Quit')) + (color_text(GREEN,30 * "-")))
                time.sleep(0.1)
                loop = False

            elif inp2 == '1':
                os.system('clear')
                ipmitool('0x30 0x30 0x01 0x01')
                print(color_text(YELLOW,17 * "-" + "Automatic Fan control turned on" + 15 * "-"))

            elif inp2 == '2':
                os.system('clear')
                ipmitool('0x30 0x30 0x02 0xff 0x00')
                print(color_text(RED,23 * "-" + "Fan Speed set to 0%" + 22 * "-"))
            
            else:
                os.system('clear')
                print(color_text(GREEN,26 * "-") + (color_text(RED,'Invalid Input')) + (color_text(GREEN,25 * "-")))
                time.sleep(0.2)
                loop = True

        elif ans in Quit:
            os.system('clear')
            print (color_text(GREEN,30 * "-") + (color_text(RED,'Quit')) + (color_text(GREEN,30 * "-")))
            time.sleep(0.1)
            loop = False
            
        else:
            os.system('clear')
            print(color_text(GREEN,26 * "-") + (color_text(RED,'Invalid Input')) + (color_text(GREEN,25 * "-")))
            time.sleep(0.2)
            loop = True

## Wrong pass ##

elif stat == 0:
    os.system('clear')
    d3raega = "Wrong Password"
    worngpwd = 27 * "-" + (color_text(RED,d3raega)) + (color_text(GREEN,26 * "-")) 
    print (color_text(GREEN,worngpwd))
    time.sleep(0.2)
    a = input("Try again? (Y/N) ")
    
    Yes = (['yes','Yes','Y','y'])
    No = (['No', 'no', 'N', 'n'])

    if a in Yes:
        os.system('python3 ipmi.py')
        time.sleep(0.3)
        sys.exit()
    elif a in No:
        print('Exit...')
        time.sleep(0.1)
        sys.exit()
else:
    print('Something went wrong.')
    sys.exit()
