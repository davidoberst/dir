# IMPORT LIBRRIES
import os
import time
import pyfiglet
from colorama import Fore, Style

# BANNER
print(Fore.RED + pyfiglet.figlet_format("dir", font="larry3d").rstrip() + Style.RESET_ALL)
print("")
print(Fore.YELLOW + "v.0.0.1 | by davidoberst | https://github.com/davidoberst" + Style.RESET_ALL)
print("-"*58)

# SELECT PATH:
while True: 
 userEntry = input(Fore.BLUE +"[::] Enter the folder path : "+ Style.RESET_ALL)
 try:
   os.chdir(userEntry)
   listpath = os.listdir(userEntry)
   break
 
 except FileNotFoundError:
    time.sleep(1)
    print(Fore.RED + "[!] Not a valid path.\n" + Style.RESET_ALL)
    time.sleep(1)
 except NotADirectoryError:
    time.sleep(1)
    print(Fore.RED + "[!] Not a valid path.\n" + Style.RESET_ALL)
    time.sleep(1)
 except PermissionError:
    time.sleep(1)
    print(Fore.RED + "[!] You dont have hacces to open this folder.\n" + Style.RESET_ALL)
    time.sleep(1)
 except OSError:
    time.sleep(1)
    print(Fore.RED + "[!] Not a valid path.\n" + Style.RESET_ALL)
    time.sleep(1)

time.sleep(1)
print(Fore.GREEN + "[::] Path founded" + Style.RESET_ALL)
time.sleep(1)
print("")
print(Fore.YELLOW + f"{'FILE':90} {'SIZE':>15}" + Style.RESET_ALL)
print(Fore.YELLOW + "-" * 120 + Style.RESET_ALL)
for x in listpath:

    full_path = os.path.join(userEntry, x) 
    size_bytes = os.path.getsize(full_path)
    isdir = os.path.isdir(x)

    
    if isdir == True:
     size_str = Fore.YELLOW + "Directory" + Style.RESET_ALL



    elif size_bytes < 1024:
        # less 1 KB → show bytes
        size_str = (Fore.WHITE + f"{size_bytes}B" + Style.RESET_ALL)

    elif size_bytes >= 1024 and size_bytes < 1024**2:
        # between 1 KB and less  1 MB → show KB
        size_kb = size_bytes / 1024
        size_str = (Fore.WHITE + f"{size_kb:.2f}KB" + Style.RESET_ALL)

    elif size_bytes >= 1024**2 and size_bytes < 1024**3:
        # between 1 MB and less 1 GB → show MB
        size_mb = size_bytes / (1024**2)
        size_str = (Fore.WHITE + f"{size_mb:.2f}MB" + Style.RESET_ALL)

    elif size_bytes >= 1024**3:
        # 1 GB or more → show GB
        size_gb = size_bytes / (1024**3)
        size_str = (Fore.WHITE + f"{size_gb:.2f}GB" + Style.RESET_ALL)
    
    
    
    
 
    time.sleep(0.1)
    print(Fore.WHITE + f"{x:90} {size_str:>15}" + Style.RESET_ALL)

 




