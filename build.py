__author__ = 'sanaes'

from distutils.core import setup
import py2exe

setup(windows=['qtTest.py'], options={"py2exe": {"includes": ["sip", "PyQt4.QtGui","PyQt4.QtCore",  "sys", "random"]}})