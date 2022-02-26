import requests, gratient
from os import system

system("cls && title Linkvertise ByPasser by UltraLion")

banner = (gratient.green("""
    __    _       __                   __  _              ____                             
   / /   (_)___  / /___   _____  _____/ /_(_)_______     / __ )__  ______  ____ ___________
  / /   / / __ \/ //_/ | / / _ \/ ___/ __/ / ___/ _ \   / __  / / / / __ \/ __ `/ ___/ ___/
 / /___/ / / / / ,<  | |/ /  __/ /  / /_/ (__  )  __/  / /_/ / /_/ / /_/ / /_/ (__  |__  ) 
/_____/_/_/ /_/_/|_| |___/\___/_/   \__/_/____/\___/  /_____/\__, / .___/\__,_/____/____/  
                                                            /____/_/                       
                            ──────  [≈] By UlraLion ──────
"""))

def purple(text):
    system(""); faded = ""
    red = 35
    for character in text:
        red += 3
        if red > 255:
            red = 255
        faded += (f"\033[38;2;{red};0;220m{character}")
    return faded

print(banner)
link = input(purple(" [»] Enter your link here : "))

try:
    data = requests.get(f"https://bypass.bot.nu/bypass2?url={link}")
    link = data.json()["destination"]
    system("cls")
    print(banner)
    print(gratient.yellow(f" [»] Link to the destination : {link}"))
except:
    system("cls")
    print(banner)
    print(gratient.red(" /!\ An unexpected error has occurred, the link you provided must be incorrect."))

system("pause >nul")