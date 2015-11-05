__author__ = 'sanaes'
import os

def killUplusApp():
    killProcessName = ['SDSMan.exe','ComAgent.exe','DSCNTSRV.EXE','PIAgent.exe','PIProtectorNS64.exe','PISupervisor.exe','PaSvc.exe']
    for kpn in killProcessName:
        print os.system('taskkill /f /im '+kpn)


killUplusApp()