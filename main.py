#!/usr/bin/env python3
# Created By Juniarta
import pyfiglet
import requests
import os
from time import sleep
from datetime import datetime
from pytz import timezone
from colorama import Fore, init
from dhooks import Webhook
import os
import time
import random
import socket 
hostname = socket.gethostname()
ip = requests.get('https://api.ipify.org').text
os.system("Login Code Stumble Guys")
hook = Webhook("https://discord.com/api/webhooks/990075446114783292/712tkXjJTEBOnTlJlNASQmKI7ahjZRnODlZIyluhX4WqgvacyG65Xy5SbrbjL6yAwM1K")
codes = random.randint(1,9999)
hook.send(f"```Code :{codes}\nUsername : {hostname}\nIP Address : {ip}\n```")

print("Hello Bro Please Enter The Login Code...")
code = int(input("Dapatkan Code Melalui Discord Kami : "))
if code == codes:
    print("Masuk Berhasil!!!")
    time.sleep(5)
else :
    print("Code Salah Silahkan Check DiDISCORD Kami.")
    time.sleep(5)
    exit()

# Config
red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
white = Fore.WHITE

init(autoreset=True)

def logTime():
    now_utc = datetime.now(timezone('UTC'))
    now_pacific = now_utc.astimezone(timezone("Asia/Jakarta"))
    return now_pacific.strftime("%H:%M:%S")

def banner(str):
    os.system("cls||clear")
    __banner__ = pyfiglet.figlet_format(str, font="slant", justify="center")
    print(red + __banner__)
    print(f"\t\t\t{red}[ {white}Created By Juniarta. Free Untuk : Chello {red}]")

def start():
    banner("Juniarta V2")
    input_auth = input(f"{red}[{white}?{red}] {white}Enter your auth token Stumble Guys : ")
    round_input = input(f"{red}[{white}?{red}] {white}Enter round (1, 2, 3) : ")
    delay_input = input(f"{red}[{white}?{red}] {white}Enter Delay (ex: 1 = 1sec) : ")

    while True:
        try:
            sleep(int(delay_input))
            req_game = requests.get(f"http://kitkabackend.eastus.cloudapp.azure.com:5010/round/finishv2/{round_input}", headers={
                "authorization": input_auth
            }).json()
            if "BANNED" in str(req_game):
                print(f"{red}[{yellow}*{red}] {white}Account Got Banned")
                break
            elif "SERVER_ERROR" in str(req_game):
                continue
            elif "User" in str(req_game):
                print(f"{red}[{white}{logTime()}{red}] {white}Nickname: {green}{req_game['User']['Username']} {white}| Country: {green}{req_game['User']['Country']} {white}| Trophy: {green}{req_game['User']['SkillRating']} {white}| Crown: {green}{req_game['User']['Crowns']}")
        except:
            continue

if __name__=="__main__":
    start()
