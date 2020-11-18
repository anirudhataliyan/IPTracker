#Imporing Modules
import requests
from termcolor import colored
import pyfiglet
import os
import json
os.system("clear")

#Writing
print ("_______________________________________________________________ ")
print((colored(pyfiglet.figlet_format("      IP-Tracker"), color="red")))
print("Twitter : @AnirudhaTaliyan")
print("Instagram : @anirudha.exe")
print("Github : @anirudhataliyan")
print ("_______________________________________________________________ ")
print()
#
#Main Program : 
ipAddr = input("Enter Your Public Ip Address : ")
url = ('http://ipinfo.io/')
r = requests.get(url+ipAddr)
print("")

diction = r.json()
for i in diction:
    print(f"{i.upper()}  :  {diction[i]}")

    
    
    
    
    
    
