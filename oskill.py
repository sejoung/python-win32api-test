__author__ = 'sanaes'
import psutil, re, os, signal

def killUplusApp():
    for pid in psutil.pids():
        p = psutil.Process(pid)
        cmd = p.cmdline()
        if cmd:
            pa = "SDS"
            s = cmd[0]
            findtext = re.findall(pa,s)
            if findtext:
                print os.kill(pid, signal.SIGBREAK)

killUplusApp()