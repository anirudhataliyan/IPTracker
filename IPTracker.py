"""
IP Tracker

This is a tool which serves the feature of fetching out information about any IP address (i.e., any computer device that is publically connected to the internet, and we just need the address of it). The tool is written in Python3.
Dependencies :
1. requests - python3 module

Usage :
1. First clone the repository from github mirror of it, using the command 'git clone https://github.com/anirudhataliyan/IPTracker/' [Type these commands in the terminal].
2. Use this command to install the dependencies - 'pip3 install -r requirements.txt'.
3. Run the script using these commands - 'python3 IPTracker.py'

Author : Anirudha Taliyan (https://github.com/anirudhataliyan/)
Created on : November 18. 2020

Last modified by : Rishav Das (https://github.com/rdofficial/)
Last modified on : May 8, 2021

Changes made in last modification :
1. Added commented docs + added more inner comments. This makes it easy for the others to read and understand the code.
2. Removed some dependencies and altered the functions served by them using the standard modules present in the python3 standard library.
3. Added a better and structured way of outputing the result of the IP tracking.
4. Added colored output feature to the tool + changed the initial heading banner (Removed the figlet version, as it was eating space and was a dependency to installed but not that significant).
5. Made a clean code base for proper reading and stuff + added more proper documentation to the project (too)
6. Removed many errors like if the response from the server was not good and all stuff. Also, prevented any future errors.

Authors contributed to this script (Add your name below if you have contributed) :
1. Anirudha Taliyan (github:https://github.com/anirudhataliyan/, email:akt746083@gmail.com)
2. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

# Importing the requird functions and modules
try:
    from os import system
    from sys import platform
    from requests import get
except Exception as e:
    # If there are any errors encountered during the importing of the modules, then we display the error on the console screen

    input(f'{red_rev}[ Error : {e} ]{defcol}\nPress enter key to continue...')
    exit()

# Defining the ANSII color codes for colored output
if 'linux' in platform:
    # If the current operating system is linux, then we continue to define the color codes

    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    blue = '\033[94m'
    red_rev = '\033[07;91m'
    yellow_rev = '\033[07;92m'
    defcol = '\033[00m'
    clear = 'clear'
else:
    red = ''
    green = ''
    yellow = ''
    blue = ''
    red_rev = ''
    yellow_rev = ''
    defcol = ''
    clear = 'cls'

def main():
    # Displaying the banner and other info
    system('clear')
    print(f'\t\t[ {yellow_rev}IP Tracker{defcol} ]\n')  # The tool name
    print(f'[{green}!{defcol}]-------------{yellow}About author{defcol}-------------[{green}!{defcol}]\n[{red}#{defcol}] Twitter : {yellow}@AnirudhaTaliyan{defcol}\n[{red}#{defcol}] Instagram : {yellow}@anirudha.exe (https://www.instagram.com/anirudha.exe/{defcol}\n[{red}#{defcol}] Github : {yellow}https://github.com/anirudhataliyan/{defcol}\n')  # The author's information
    print(f'[{green}!{defcol}]-----------------{yellow}Note{defcol}-----------------[{green}!{defcol}]\n[{red}1{defcol}] Make sure you are connected to internet.\n[{red}2{defcol}] Make sure the IP address you are looking is a public IP.\n[{red}3{defcol}] If you want to stop the script in the middle, then press CTRL+C key combo.\n')

    # Asking the user to enter the IP Address
    ipAddress = input('Enter the IP address : ')

    # Checking if the user entered blank value or not
    if len(ipAddress) == 0:
        # If the user entered value is blank, then we display the error on the console screen

        input(f'{red_rev}[ Error : {e} ]{defcol}\nPress enter key to continue...')
        return 0
    else:
        # If the user entered value is not blank, then we continue

        response = get(f'http://ipinfo.io/{ipAddress}')
        if response.status_code == 200:
            # If the response we recieved indicates successfull HTTP request

            response = response.json()
            for item in response:
                print(f'[{green}#{defcol}] %-25s    :    {yellow}%-25s{defcol}' %(item.upper(), response[item]))
        else:
            # If the response we recieved indicates failed HTTP request, then we display the error on the console screen

            input(f'{red_rev}[ Error : Failed to fetch the information about the specified IP address ]{defcol}\nPress enter key to continue...')
            return 0

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        # If the user presses CTRL+C key combo, then we exit

        exit()
    except Exception as e:
        # If we encounter any error during the process, then we display the error on the console screen

        input(f'{red_rev}[ Error : {e} ]{defcol}\nPress enter key to continue...')
        exit()
