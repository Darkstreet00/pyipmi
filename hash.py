#!/usr/bin/env python3

import bcrypt
import os
import json
import time
import sys

GREEN = "32m"

def color_text(color, text):
    colored_text = f"\033[{color}{text}\033[00m"
    return colored_text

ip = input("IP/DOMAIN: ")
user = input("User: ")
passwd = input("Enter your password: ").encode("utf-8")

hashedpasswd = bcrypt.hashpw(passwd, bcrypt.gensalt()).decode("utf-8")

print(color_text(GREEN, "Password hash generated."))
time.sleep(0.1)

config = {
"ip": ip,
"user": user,
"pass": hashedpasswd
}

with open('config.json', 'w') as json_file:
  json.dump(config, json_file)
time.sleep(0.3)


print(color_text(GREEN, "Config file created."))

time.sleep(0.5)
sys.exit()
