# -*- coding: utf-8 -*-

# A simple setup script to create an executable using PyQt4. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# PyQt4app.py is a very simple type of PyQt4 application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'icon' : 'images/applications_games.ico',
        'excludes' : [
            'PyQt4.QtXml',
            'PyQt4.QtTest',
            'PyQt4.QtSvg',
            'PyQt4.QtSql',
            'PyQt4.QtScript',
            'PyQt4.QtOpenGL',
            'PyQt4.QtNetwork',
            'PyQt4.Qsci',
            '_bz2',
            '_hashlib',
            '_ssl'
        ]       
    }
}

executables = [
    Executable('testsuite.pyw', base=base)
]

setup(name='TestSuite',
      version='2.3',
      description='TestSuite for Manual Mode',
      options=options,
      executables=executables
      )
