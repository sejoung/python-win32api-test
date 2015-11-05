__author__ = 'sanaes'
import psutil, subprocess
import sys, os, traceback, types

def killApp():
    killProcessName = ['sdslogin.exe', 'sdsman.exe', 'comagent.exe', 'dscntsrv.exe', 'piagent.exe',
                       'piprotectorns64.exe', 'pisupervisor.exe', 'patray.exe', 'pasvc.exe', 'secupc.exe']
    for p in psutil.process_iter():
        for kpn in killProcessName:
            if p.name().upper() == kpn.upper():
                print p.kill
                print p.terminate()


def processList():
    for p in psutil.process_iter():
        cmd = p.cmdline()
        if (cmd):
            print cmd


def liveApp():
    print subprocess.call("C:\\Windows\\Softcamp\\SDS\\SDSMan.exe", shell=True)


killApp()