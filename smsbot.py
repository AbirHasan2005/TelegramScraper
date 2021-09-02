#!/bin/env python3
# Modified by @AbirHasan2005
# Telegram Group: http://t.me/linux_repo
# Please give me credits if you use any codes from here.


from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
import configparser
import os, sys
import csv
import random
import time

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
yo="\033[1;33m"
SLEEP_TIME = 30

class main():

    def banner():
        
        print(f"""
    {re}╔╦╗{cy}┌─┐┬  ┌─┐{re}╔═╗  ╔═╗{cy}┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
    {re} ║ {cy}├┤ │  ├┤ {re}║ ╦  ╚═╗{cy}│  ├┬┘├─┤├─┘├┤ ├┬┘
    {re} ╩ {cy}└─┘┴─┘└─┘{re}╚═╝  ╚═╝{cy}└─┘┴└─┴ ┴┴  └─┘┴└─

                Version: 1.3
         Modified by @AbirHasan2005
            """)

    def send_sms():
        try:
            cpass = configparser.RawConfigParser()
            cpass.read('config.data')
            api_id = cpass['cred']['id']
            api_hash = cpass['cred']['hash']
            phone = cpass['cred']['phone']
        except KeyError:
            os.system('clear')
            main.banner()
            print("\033[91m[!] Please run \033[92mpython3 setup.py\033[91m first !!!\033[0m\n")
            sys.exit(1)

        client = TelegramClient(phone, api_id, api_hash)

        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone)
            os.system('clear')
            main.banner()
            client.sign_in(phone, input(gr+'[+] Enter the sent code: '+re))

        os.system('clear')
        main.banner()
        input_file = sys.argv[1]
        users = []
        with open(input_file, encoding='UTF-8') as f:
            rows = csv.reader(f,delimiter=",",lineterminator="\n")
            next(rows, None)
            for row in rows:
                user = {
                    'username': row[0],
                    'id': int(row[1]),
                    'access_hash': int(row[2]),
                    'name': row[3],
                }

                users.append(user)
        print(gr+"[1] Send SMS by user ID\n[2] Send SMS by username ")
        mode = int(input(gr+"Input: "+re))

        message = input(gr+"[+] Enter Your Message: "+yo)

        for user in users:
            if mode == 1:
                receiver = InputPeerUser(user['id'],user['access_hash'])
            elif mode == 2:
                if user['username'] == "":
                    continue
                receiver = client.get_input_entity(user['username'])
            else:
                print(re+"[!] Invalid Mode. Exiting ...")
                client.disconnect()
                sys.exit()
            try:
                print(gr+"[+] Sending Message to:", user['name'])
                client.send_message(receiver, message.format(user['name']))
                print(gr+"[+] Waiting {} seconds".format(SLEEP_TIME))
                time.sleep(SLEEP_TIME)
            except PeerFloodError:
                print(re+"[!] Getting Flood Errors from Telegram. \n[!] Script is stopping for now. \n[!] Please try again after some time.")
                client.disconnect()
                sys.exit()
            except Exception as e:
                print(re+"[!] Error:", e)
                print(re+"[!] Trying to continue ...")
                continue
        client.disconnect()
        print("Done. Message sent to all users.")



main.send_sms()