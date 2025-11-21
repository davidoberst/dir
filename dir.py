# IMPORT LIBRRIES
import os
import time
import pyfiglet


# BANNER
print(pyfiglet.figlet_format("dir", font="larry3d").rstrip())
print("")
print("v.0.0.1 | by davidoberst | https://github.com/davidoberst")
print("-"*58)

# SELECT PATH:
while True: 
 
 userEntry = input("[::] Enter the folder path : ")
 try:
   os.chdir(userEntry)
   listpath = os.listdir(userEntry)
   break
 
 except FileNotFoundError:
    time.sleep(1)
    print("[!] Not a valid path.\n")
    time.sleep(1)
 except NotADirectoryError:
    time.sleep(1)
    print("[!] Not a valid path.\n")
    time.sleep(1)
 except PermissionError:
    time.sleep(1)
    print("[!] You dont have hacces to open this folder.\n")
    time.sleep(1)
 except OSError:
    time.sleep(1)
    print("[!] Not a valid path.\n")
    time.sleep(1)

time.sleep(1)
print("[::] Path founded")
time.sleep(1)
print("")
print(f"{'FILE':90} {'SIZE':>15}")
print("-" * 120)
for x in listpath:

    full_path = os.path.join(userEntry, x) 
    size_bytes = os.path.getsize(full_path)
    isdir = os.path.isdir(x)

    
    if isdir == True:
     size_str = (f"Directory")

    elif size_bytes < 1024:
        # less 1 KB → show bytes
        size_str = (f"{size_bytes}B")

    elif size_bytes >= 1024 and size_bytes < 1024**2:
        # between 1 KB and less  1 MB → show KB
        size_kb = size_bytes / 1024
        size_str = (f"{size_kb:.2f}KB")

    elif size_bytes >= 1024**2 and size_bytes < 1024**3:
        # between 1 MB and less 1 GB → show MB
        size_mb = size_bytes / (1024**2)
        size_str = (f"{size_mb:.2f}MB")

    elif size_bytes >= 1024**3:
        # 1 GB or more → show GB
        size_gb = size_bytes / (1024**3)
        size_str = (f"{size_gb:.2f}GB")
    
    
    
    
 
    time.sleep(0.1)
    print(f"{x:90} {size_str:>15}")

 




