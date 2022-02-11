###IP TRACKER ###
import requests
import argparse
import json
from colorama import Fore , init

init(convert=True,autoreset=True)

args = None
p = argparse.ArgumentParser(description='IP Tracker. Usage: ip.py -ip <IP>')
p.add_argument('-ip', metavar='IP', type=str,help='ip target')
args = p.parse_args()

ip = args.ip

API_URL = 'https://ipapi.co/'+ip+'/json/'
print('Scanning:' + ' ' + ip)

r = requests.get(API_URL)
json = json.loads(r.text)

print(Fore.GREEN +'IP: ' + json['ip'])
print(Fore.GREEN +'City: ' + json['city'])
print(Fore.GREEN +'Region:  ' + json['region'])
print(Fore.GREEN +'Country: ' + json['country_name'])
