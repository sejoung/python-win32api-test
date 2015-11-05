__author__ = 'sanaes'
from distutils.core import setup
import py2exe

setup(windows=['killAppUi.py'], options={'py2exe': {'includes': ['psutil','subprocess','sys','PyQt4.QtCore','PyQt4.QtGui','sip', 'os', 'signal']}})