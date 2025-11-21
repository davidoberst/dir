# IMPORT LIBRRIES
import os
import pyfiglet

# BANNER
print(pyfiglet.figlet_format("dir", font="larry3d").rstrip())
print("")
print("v.0.0.1 | by davidoberst | https://github.com/davidoberst")
print("-"*58)

# SELECT PATH:
userEntry = input("[::] Enter the folder path : ")
os.chdir(userEntry)
listpath = os.listdir(userEntry)

def listFilesAndShowSize():
 for x in listpath:
    full_path = os.path.join(userEntry, x) 
    size_bytes = os.path.getsize(full_path)

    if size_bytes < 1024:
        # less 1 KB → show bytes
        print(f"{x}  {size_bytes} B")

    elif size_bytes >= 1024 and size_bytes < 1024**2:
        # between 1 KB and less  1 MB → show KB
        size_kb = size_bytes / 1024
        print(f"{x}  {size_kb:.2f} KB")

    elif size_bytes >= 1024**2 and size_bytes < 1024**3:
        # between 1 MB and less 1 GB → show MB
        size_mb = size_bytes / (1024**2)
        print(f"{x}  {size_mb:.2f} MB")

    elif size_bytes >= 1024**3:
        # 1 GB or more → show GB
        size_gb = size_bytes / (1024**3)
        print(f"{x}  {size_gb:.2f} GB")


 




