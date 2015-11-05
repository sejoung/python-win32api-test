import sys, psutil, subprocess, os, signal
from PyQt4 import QtCore, QtGui


class KillApp(QtGui.QMainWindow):

    def __init__(self):
        super(KillApp, self).__init__()

        self.initUI()

    def initUI(self):

        btn1 = QtGui.QPushButton("kill", self)
        btn1.move(0, 200)
        btn2 = QtGui.QPushButton("live", self)
        btn2.move(100, 200)
        btn3 = QtGui.QPushButton("runlist", self)
        btn3.move(200, 200)

        self.textBrowser = QtGui.QTextBrowser(self)
        self.textBrowser.move(30, 10)
        self.textBrowser.setFixedSize(250,180)
        btn1.clicked.connect(self.KillButtonClicked)
        btn2.clicked.connect(self.LiveButtonClicked)
        btn3.clicked.connect(self.ListButtonClicked)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('killApp')
        self.show()

    def KillButtonClicked(self):
        killProcessName = ['sdslogin.exe', 'sdsman.exe', 'comagent.exe', 'dscntsrv.exe', 'piagent.exe',
                           'piprotectorns64.exe', 'pisupervisor.exe', 'patray.exe', 'pasvc.exe', 'secupc.exe']
        self.textBrowser.setText('kill start')

        for p in psutil.process_iter():
            for kpn in killProcessName:
                if p.name().upper() == kpn.upper():
                    os.kill(p.pid, signal.SIGBREAK)
                    self.textBrowser.append(kpn +' kill')

        self.textBrowser.append('kill end')

    def LiveButtonClicked(self):
        subprocess.call("C:\\Windows\\Softcamp\\SDS\\ComAgent.exe", shell=True)
        subprocess.call("C:\\Windows\\Softcamp\\SDS\\SDSMan.exe", shell=True)
        subprocess.call("C:\\Windows\\Softcamp\\SDS\\SDSLogin.exe", shell=True)
        self.textBrowser.setText('live ok')

    def ListButtonClicked(self):
        self.textBrowser.setText('list')
        for p in psutil.process_iter():
            cmd = p.cmdline()
            if (cmd):
                self.textBrowser.append(cmd[0])



def main():
    app = QtGui.QApplication(sys.argv)
    ex = KillApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
