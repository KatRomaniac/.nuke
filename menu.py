#---------------------------------
# menu.py
# Version: 1.0.0
# Last Updated: July 27th, 2023
#---------------------------------

import nuke
import platform

#.Deine where .nuke directory is on each OS's network

Win_Dir = 'C:\Users\Kasha/.nuke'

MacOSX_Dire = ''
Linux_Dir = '/home/Kasha/.nuke'

# Set global directory

if platform.system() == "Windows":
	dir = Win_Dir
elif platform.system() == "Darwin":
	dir = MacOSX_Dir
elif platform.system() == "Linux":
	dir = Linux_Dir
else:
	dir = None
