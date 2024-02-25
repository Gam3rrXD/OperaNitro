from colorama import Fore
import requests
import os
from time import sleep
import random
import string
from datetime import datetime
methods = ["Single Code" , "Multi-Code Generator", "Exit"]
headers = {
    "authority": "api.discord.gx.games",
    "accept": "*/*",
    "content-type": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "origin": "https://www.opera.com",
    "referer": "https://www.opera.com/",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Opera GX";v="106"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0"
}
logo = """ 
     .d88b.  d8888b. d88888b d8888b.  .d8b.       d8b   db d888888b d888888b d8888b.  .d88b.  
    .8P  Y8. 88  `8D 88'     88  `8D d8' `8b      888o  88   `88'   `~~88~~' 88  `8D .8P  Y8. 
    88    88 88oodD' 88ooooo 88oobY' 88ooo88      88V8o 88    88       88    88oobY' 88    88 
    88    88 88~~~   88~~~~~ 88`8b   88~~~88      88 V8o88    88       88    88`8b   88    88 
    `8b  d8' 88      88.     88 `88. 88   88      88  V888   .88.      88    88 `88. `8b  d8' 
     `Y88P'  88      Y88888P 88   YD YP   YP      VP   V8P Y888888P    YP    88   YD  `Y88P'
                            Created By Gam3rr [https://github.com/Gam3rrXD]\n"""
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def genuid():
    uid = ''.join(random.choices(string.ascii_lowercase + string.digits, k=64))
    data = {
        "partnerUserId": uid
    }
    return data
def main():
    clear()
    curr = datetime.now()
    end = datetime(2024, 7, 17)
    if curr > end or curr == end:
        os.system('title Nitro Gen ~ Opera Method ~ Program Discontinued')
        print(Fore.RED + logo)
        print(Fore.LIGHTMAGENTA_EX + f"This program is discontinued since the promotion has ended! | Todays date [{curr.strftime('%B %d, %Y')}] | Promotion end date [July 16, 2024]")
        print(Fore.WHITE + "Press any key to exit")
        input("")
        os.system('exit')
    else:
        os.system('title Nitro Gen ~ Opera Method ~ Main Menu')
        print(Fore.RED + logo)
        for i in range(len(methods)):
            print(Fore.WHITE + "[", end="")
            print(Fore.RED + str(i), end="")
            print(Fore.WHITE + "] ", end="")
            print(methods[i])
        f = input("")
        match f:
            case "0":
                singlecode()
            case "1":
                multi()
            case "2":
                os.system('exit')
            case _:
                print(Fore.RED+ "Invalid Option!")
                sleep(1)
                main()
def singlecode():
    os.system('title Nitro Gen ~ Opera Method ~ Single Mode')
    clear()
    print(Fore.RED + logo)
    al = requests.post("https://api.discord.gx.games/v1/direct-fulfillment", json=genuid(), headers=headers)
    token = al.json()["token"]
    print("Your Code is: " + Fore.WHITE + f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}")
    print(Fore.GREEN + "Hit any key to return to main menu!")
    input("")
    main()
def multi():
     os.system('title Nitro Gen ~ Opera Method ~ Multi Mode')
     clear()
     print(Fore.RED + logo)
     ff = input("Enter file name: ")
     am = input("Enter amount of codes: ")
     for i in range(int(am)):
        al = requests.post("https://api.discord.gx.games/v1/direct-fulfillment", json=genuid(), headers=headers)
        token = al.json()["token"]
        with open(ff, "a") as d:
            d.writelines(f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}\n")
            d.close()
        print(f"{i +1} lines written!")
     print(Fore.GREEN + "Hit any key to return to main menu!")
     input("")
     main()
main()
