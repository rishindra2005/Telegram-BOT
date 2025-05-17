# Inside script.py
import os
import requests
import time
global mec 
mec = False
global net
net= False
while True:
    try:
        requests.get("https://www.google.com", timeout=5)
        net= True
    except requests.ConnectionError:
        net= False

    if mec==False and net == True:
        # Start your service here (if not already running)
        os.system("sudo systemctl start V")
        os.system("sudo systemctl start R")
        mec=True
    if mec==True and net==False:
        # Stop your service here (if running)
        os.system("sudo systemctl stop V")
        os.system("sudo systemctl Stop R")
        mec=False
    time.sleep(30)
    
