import requests 
import string
import logging
import os
import threading
import secrets
import random
from pystyle import Colors, Colorate

from threading import Thread
from colorama import Fore

os.system("title [the 500] - vortex & mode 40, 40")

logging.basicConfig(
    level=logging.INFO,
    format=f"[%(asctime)s]%(message)s ",
    datefmt="%H:%M:%S"
)

def email(char_num):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(char_num))

def vortex(email):
    for i in range(500):
        r = requests.Session()

        r = requests.get('http://46.101.168.188:5000/emails/' + email(10) + "@gmail.com" + '/619F5E1375AC225A44F656FD7AE58')

        if r.status_code == 200:
            logging.info(Colorate.Horizontal(Colors.blue_to_cyan, f" Succesfully sent one license key {r.status_code}"))

        else:
            logging.info(Colorate.Horizontal(Colors.yellow_to_red, f" Unknown Error {r.status_code}"))



threads = []

for _ in range(100):
    threads.append(Thread(target=vortex, args=[email]))

for x in threads:
    x.start()

for x in threads:
    x.join()
